##
#     Project: Django dnsmasq
# Description: A Django application to create dnsmasq configuration
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2021 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import argparse

from django.core.management.base import BaseCommand
from django.utils.translation import pgettext_lazy

from dnsmasq.constants import MAC_ADDRESS_ZEROS, MAC_ADDRESS_ANY
from dnsmasq.models import (Action,
                            DhcpHost,
                            DhcpOption,
                            DhcpOptionType,
                            DhcpRange,
                            Domain,
                            Interface,
                            ListenAddress,
                            Option)
from project import PRODUCT_NAME, VERSION


class Command(BaseCommand):
    help = 'Create configuration for dnsmasq'

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        BaseCommand.add_arguments(self, parser)
        parser.add_argument('--filename',
                            action='store',
                            type=str,
                            required=True,
                            help=pgettext_lazy(
                                'CreateConfiguration',
                                'Configuration filename'))
        parser.add_argument('--descriptions',
                            action='store_true',
                            required=False,
                            help=pgettext_lazy(
                                'CreateConfiguration',
                                'Include descriptions'))

    def handle(self, *args, **options) -> None:
        """
        Create configuration file
        """
        def add_header(title: str) -> None:
            """
            Add section header to the configuration file

            :param title: section title
            """
            separator = '-' * 77
            file.write(f'\n# {separator}\n# {title}\n# {separator}\n')

        def add_description(name: str, description: str) -> None:
            """
            Add name and description to the configuration file

            :param name: option name
            :param description: option description
            """
            if include_descriptions and (description or name):
                if name and description:
                    file.write(f'# {name}: {description}\n')
                elif name:
                    file.write(f'# {name}\n')
                else:
                    file.write(f'# {description}\n')

        def get_option_value(option: DhcpOption) -> str:
            """
            Get value for a DhcpOption object

            :param option: DHCP option to check
            :return: resulting value
            """
            if option.option.type in (DhcpOptionType.IPV4_X1,
                                      DhcpOptionType.IPV4_X2,
                                      DhcpOptionType.IPV4_MANY):
                options = option.dhcpoptionipv4_set.order_by('order')
                if option.option.type == DhcpOptionType.IPV4_X1:
                    # Use only the first value
                    options = options[:1]
                elif option.option.type == DhcpOptionType.IPV4_X2:
                    # Use only the first two values
                    options = options[:2]
                # Format values
                results = ','.join(option.address
                                   for option
                                   in options)
            elif option.option.type == DhcpOptionType.CHARACTER:
                results = option.character_value
            else:
                results = str(option.numeric_value)
            return results

        include_descriptions = options['descriptions']
        with open(options['filename'], mode='w') as file:
            # Create the configuration file
            file.write(f'# Configuration file for dnsmasq created '
                       f'automatically by '
                       f'{PRODUCT_NAME} v.{VERSION}\n')
            file.write('# Please do not edit this file directly\n')
            # Active Interfaces
            if queryset := Interface.objects_enabled.filter(excluded=False):
                add_header('Active interfaces')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'interface={item.name}\n')
            # Excluded Interfaces
            if queryset := Interface.objects_enabled.filter(excluded=True):
                add_header('Excluded Interfaces')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'except-interface={item.name}\n')
            # No DHCP Interfaces
            if queryset := Interface.objects_enabled.filter(disable_dhcp=True):
                add_header('No DHCP Interfaces')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'no-dhcp-interface={item.name}\n')
            # Listen addresses
            if queryset := ListenAddress.objects_enabled.all():
                add_header('Listening addresses')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'listen-address={item.address}\n')
            # Actions
            if queryset := Action.objects_enabled.all():
                add_header('Actions')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'{item.action}\n')
            # Options
            if queryset := Option.objects_enabled.all():
                add_header('Options')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'{item.option}={item.value}\n')
            # Domains
            if queryset := Domain.objects_enabled.all():
                add_header('Domains')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'domain={item.name}')
                    if item.subnet_ip:
                        file.write(f',{item.subnet_ip}/{item.subnet_cidr}')
                    if item.starting_ip:
                        file.write(f',{item.starting_ip},{item.ending_ip}')
                    file.write('\n')
            # DHCP ranges
            if queryset := DhcpRange.objects_enabled.all():
                add_header('DHCP ranges')
                for item in queryset.order_by('order'):
                    add_description(item.name, item.description)
                    file.write(f'dhcp-range={item.starting_ip},'
                               f'{item.ending_ip},'
                               f'{item.lease_time}h\n')
            # DHCP default options
            if queryset := DhcpOption.objects_enabled.filter(forced=False):
                add_header('DHCP default options')
                for item in queryset:
                    add_description(item.option.name, item.option.description)
                    value = get_option_value(option=item)
                    file.write(f'dhcp-option={item.option.option},{value}\n')
            # DHCP forced default options
            if queryset := DhcpOption.objects_enabled.filter(forced=True):
                add_header('DHCP forced default options')
                for item in queryset:
                    add_description(item.option.name, item.option.description)
                    value = get_option_value(option=item)
                    file.write(f'dhcp-option-force={item.option.option},'
                               f'{value}\n')
            # Ignored DHCP hosts
            if queryset := DhcpHost.objects_enabled.filter(ignored=True):
                add_header('Ignored hosts')
                for item in queryset:
                    add_description(item.name, item.description)
                    mac_address = (item.mac_address
                                   if item.mac_address != MAC_ADDRESS_ZEROS
                                   else MAC_ADDRESS_ANY)
                    file.write(f'dhcp-host={mac_address},ignore\n')
            # Allowed DHCP hosts
            if queryset := DhcpHost.objects_enabled.filter(ignored=False):
                add_header('Allowed hosts')
                for item in queryset:
                    add_description(item.name, item.description)
                    mac_address = (item.mac_address
                                   if item.mac_address != MAC_ADDRESS_ZEROS
                                   else MAC_ADDRESS_ANY)
                    file.write(f'dhcp-host={mac_address}\n')
