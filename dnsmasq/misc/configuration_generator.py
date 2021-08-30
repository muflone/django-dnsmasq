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

from dnsmasq.constants import (DISABLED_OPTION_PREFIX,
                               MAC_ADDRESS_ZEROS,
                               MAC_ADDRESS_ANY)
from dnsmasq.models import (DhcpHost,
                            DhcpOption,
                            DhcpOptionType,
                            DhcpRange,
                            DhcpTag,
                            Domain,
                            Interface,
                            ListenAddress,
                            Option)

from project import PRODUCT_NAME, VERSION

SECTION_HEADERS = 'headers'
SECTION_OPTIONS = 'options'
SECTION_INTERFACES = 'interfaces'
SECTION_LISTEN_ADDRESSES = 'listen_addresses'
SECTION_DOMAINS = 'domains'
SECTION_DHCP_RANGES = 'dhcp_ranges'
SECTION_DHCP_OPTIONS = 'dhcp_options'
SECTION_DHCP_HOSTS = 'dhcp_hosts'


class ConfigurationGenerator(object):
    def __init__(self, include_descriptions: bool, show_disabled: bool):
        self.include_descriptions = include_descriptions
        self.show_disabled = show_disabled
        self.configuration_blocks_map = {
            SECTION_HEADERS: self.process_headers,
            SECTION_OPTIONS: self.process_options,
            SECTION_INTERFACES: self.process_interfaces,
            SECTION_LISTEN_ADDRESSES: self.process_listen_addresses,
            SECTION_DOMAINS: self.process_domains,
            SECTION_DHCP_RANGES: self.process_dhcp_ranges,
            SECTION_DHCP_OPTIONS: self.process_dhcp_options,
            SECTION_DHCP_HOSTS: self.process_dhcp_hosts
        }

    @staticmethod
    def add_header(title: str) -> str:
        """
        Add section header to the configuration file

        :param title: section title
        :return: header description
        """
        separator = '-' * 77
        return f'\n# {separator}\n# {title}\n# {separator}'

    def add_description(self, name: str, description: str) -> str:
        """
        Add name and description to the configuration file

        :param name: option name
        :param description: option description
        :return: resulting description
        """
        results = None
        if self.include_descriptions and (description or name):
            if name and description:
                results = f'# {name}: {description}'
            elif name:
                results = f'# {name}'
            else:
                results = f'# {description}'
        return results

    @staticmethod
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

    @staticmethod
    def format_results(results: list[str]) -> str:
        """
        Format a results list from any process_* function to a string
        :param results: results lists
        :return: formatted string from results
        """
        return '\n'.join(filter(lambda line: line is not None, results))

    def process_headers(self):
        """
        Export the configuration options headers
        """
        results = []
        results.append(f'# Configuration file for dnsmasq created '
                       f'automatically by '
                       f'{PRODUCT_NAME} v.{VERSION}')
        results.append('# Please do not edit this file directly')
        return results

    def process_interfaces(self):
        """
        Export the configuration options for interfaces
        """
        results = []
        line_items = []
        # Active Interfaces
        manager = (Interface.objects
                   if self.show_disabled
                   else Interface.objects_enabled)
        if queryset := manager.filter(excluded=False):
            results.append(self.add_header('Active interfaces'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'interface={item.name}')
                results.append(''.join(line_items))
        # Excluded Interfaces
        if queryset := manager.filter(excluded=True):
            results.append(self.add_header('Excluded Interfaces'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'except-interface={item.name}')
                results.append(''.join(line_items))
        # No DHCP Interfaces
        if queryset := manager.filter(disable_dhcp=True):
            results.append(self.add_header('No DHCP Interfaces'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'no-dhcp-interface={item.name}')
                results.append(''.join(line_items))
        return results

    def process_listen_addresses(self):
        """
        Export the configuration options for listen addresses
        """
        results = []
        line_items = []
        manager = (ListenAddress.objects
                   if self.show_disabled
                   else ListenAddress.objects_enabled)
        if queryset := manager.all():
            results.append(self.add_header('Listening addresses'))
            for item in queryset:
                results.append(self.add_description(item.address,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'listen-address={item.address}')
                results.append(''.join(line_items))
        return results

    def process_options(self):
        """
        Export the configuration options for options
        """
        results = []
        line_items = []
        manager = (Option.objects
                   if self.show_disabled
                   else Option.objects_enabled)
        if queryset := manager.all():
            results.append(self.add_header('Options'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                # Option name
                line_items.append(f'{item.option}')
                if len(item.value):
                    # Option with value
                    line_items.append(f'={item.value}')
                results.append(''.join(line_items))
        return results

    def process_domains(self):
        """
        Export the configuration options for domains
        """
        results = []
        line_items = []
        manager = (Domain.objects
                   if self.show_disabled
                   else Domain.objects_enabled)
        if queryset := manager.all():
            results.append(self.add_header('Domains'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'domain={item.name}')
                if item.subnet_ip:
                    line_items.append(f',{item.subnet_ip}/{item.subnet_cidr}')
                if item.starting_ip:
                    line_items.append(f',{item.starting_ip},{item.ending_ip}')
                results.append(''.join(line_items))
        return results

    def process_dhcp_ranges(self):
        """
        Export the configuration options for DHCP ranges
        """
        results = []
        line_items = []
        manager = (DhcpRange.objects
                   if self.show_disabled
                   else DhcpRange.objects_enabled)
        if queryset := manager.all():
            results.append(self.add_header('DHCP ranges'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-range={item.starting_ip},'
                                  f'{item.ending_ip},'
                                  f'{item.lease_time}m')
                results.append(''.join(line_items))
        return results

    def process_dhcp_options(self):
        """
        Export the configuration options for DHCP options
        """
        results = []
        line_items = []
        # DHCP default options
        manager = (DhcpOption.objects
                   if self.show_disabled
                   else DhcpOption.objects_enabled)
        if queryset := manager.filter(tag__name=DhcpTag.DEFAULT_TAG,
                                      forced=False):
            results.append(self.add_header('DHCP default options'))
            for item in queryset:
                results.append(self.add_description(item.option.name,
                                                    item.option.description))
                value = self.get_option_value(option=item)
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-option={item.option.option},{value}')
                results.append(''.join(line_items))
        # DHCP forced default options
        if queryset := manager.filter(tag__name=DhcpTag.DEFAULT_TAG,
                                      forced=True):
            results.append(self.add_header('DHCP forced default options'))
            for item in queryset:
                results.append(self.add_description(item.option.name,
                                                    item.option.description))
                value = self.get_option_value(option=item)
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-option-force={item.option.option},'
                                  f'{value}')
                results.append(''.join(line_items))
        # DHCP options for tags
        if queryset := manager.filter(forced=False).exclude(
                tag__name=DhcpTag.DEFAULT_TAG):
            results.append(self.add_header('DHCP options for tags'))
            last_tag_id = None
            for item in queryset:
                # Skip duplicated tags description
                if last_tag_id != item.tag_id:
                    # Add line separator between tags
                    if last_tag_id is not None:
                        results.append('')
                    results.append(self.add_description(item.tag.name,
                                                        item.tag.description))
                    last_tag_id = item.tag_id
                results.append(self.add_description(item.option.name,
                                                    item.option.description))
                value = self.get_option_value(option=item)
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-option=tag:{item.tag.name},'
                                  f'{item.option.option},{value}')
                results.append(''.join(line_items))
        # DHCP forced options for tags
        if queryset := manager.filter(forced=True).exclude(
                tag__name=DhcpTag.DEFAULT_TAG):
            results.append(self.add_header('DHCP forced options for tags'))
            last_tag_id = None
            for item in queryset:
                # Skip duplicated tags description
                if last_tag_id != item.tag_id:
                    # Add line separator between tags
                    if last_tag_id is not None:
                        results.append('')
                    results.append(self.add_description(item.tag.name,
                                                        item.tag.description))
                    last_tag_id = item.tag_id
                results.append(self.add_description(item.option.name,
                                                    item.option.description))
                value = self.get_option_value(option=item)
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-option-force=tag:{item.tag.name},'
                                  f'{item.option.option},{value}')
                results.append(''.join(line_items))
        return results

    def process_dhcp_hosts(self):
        """
        Export the configuration options for DHCP hosts
        """
        results = []
        line_items = []
        # Ignored DHCP hosts
        manager = (DhcpHost.objects
                   if self.show_disabled
                   else DhcpHost.objects_enabled)
        if queryset := manager.filter(ignored=True):
            results.append(self.add_header('Ignored hosts'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                mac_address = (item.mac_address
                               if item.mac_address != MAC_ADDRESS_ZEROS
                               else MAC_ADDRESS_ANY)
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-host={mac_address},ignore')
                results.append(''.join(line_items))
        # Allowed DHCP hosts
        if queryset := manager.filter(ignored=False):
            results.append(self.add_header('Allowed hosts'))
            for item in queryset:
                results.append(self.add_description(item.name,
                                                    item.description))
                mac_address = (item.mac_address
                               if item.mac_address != MAC_ADDRESS_ZEROS
                               else MAC_ADDRESS_ANY)
                # Add DHCP Host
                line_items.clear()
                if not item.is_active:
                    line_items.append(DISABLED_OPTION_PREFIX)
                line_items.append(f'dhcp-host={mac_address}')
                if item.tag and item.tag.name != DhcpTag.DEFAULT_TAG:
                    # Add tag
                    line_items.append(f',set:{item.tag}')
                if item.address:
                    # Add IP address
                    line_items.append(f',{item.address}')
                if item.hostname:
                    # Add hostname
                    line_items.append(f',{item.hostname}')
                if item.lease_time > 0:
                    # Add lease time
                    line_items.append(f',{item.lease_time}m')
                elif item.lease_time < 0:
                    # Add infinite lease time
                    line_items.append(',infinite')
                results.append(''.join(line_items))
        return results
