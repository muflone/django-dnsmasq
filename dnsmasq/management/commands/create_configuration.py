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

from dnsmasq.misc.configuration_generator import ConfigurationGenerator


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
        parser.add_argument('--disabled',
                            action='store_true',
                            required=False,
                            help=pgettext_lazy(
                                'CreateConfiguration',
                                'Show disabled options'))

    def handle(self, *args, **options) -> None:
        """
        Create configuration file
        """
        configuration = ConfigurationGenerator(
            include_descriptions=options['descriptions'],
            include_disabled=options['disabled'])
        # Save configuration
        with open(options['filename'], mode='w') as file:
            file.write(configuration.process())
            file.write('\n')
            file.write('\n')
