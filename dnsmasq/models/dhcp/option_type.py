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

from django.db import models
from django.utils.translation import pgettext_lazy

from utility.models import (BaseModel, BaseModelAdmin,
                            ManagerEnabled, ManagerDisabled)


class DhcpOptionType(BaseModel):
    """
    DHCP Option types
    """
    CHARACTER = 'char'
    BOOLEAN = 'bool'
    INTEGER_SHORT = 'int1'
    INTEGER = 'int2'
    INTEGER_LONG = 'int4'
    IPV4_X1 = 'ipv4x1'
    IPV4_X2 = 'ipv4x2'
    IPV4_MANY = 'ipv4'
    NAMES = {CHARACTER: pgettext_lazy('DhcpOptionType',
                                      'Character'),
             BOOLEAN: pgettext_lazy('DhcpOptionType',
                                    'Boolean'),
             INTEGER_SHORT: pgettext_lazy('DhcpOptionType',
                                          'Dhort integer'),
             INTEGER: pgettext_lazy('DhcpOptionType',
                                    'Integer'),
             INTEGER_LONG: pgettext_lazy('DhcpOptionType',
                                         'Long integer'),
             IPV4_X1: pgettext_lazy('DhcpOptionType',
                                    'Single IPv4 address'),
             IPV4_X2: pgettext_lazy('DhcpOptionType',
                                    'Double IPv4 addresses'),
             IPV4_MANY: pgettext_lazy('DhcpOptionType',
                                      'Multiple IPv4 addresses')
             }

    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name=pgettext_lazy(
                                'DhcpOptionType',
                                'name'))
    option = models.PositiveIntegerField(unique=True,
                                         verbose_name=pgettext_lazy(
                                             'DhcpOptionType',
                                             'option'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'DhcpOptionType',
                                       'description'))
    type = models.CharField(max_length=10,
                            choices=(
                                (CHARACTER, pgettext_lazy('DhcpOptionType',
                                                          'character')),
                                (BOOLEAN, pgettext_lazy('DhcpOptionType',
                                                        'boolean')),
                                (INTEGER_SHORT, pgettext_lazy('DhcpOptionType',
                                                              'numeric byte')),
                                (INTEGER, pgettext_lazy('DhcpOptionType',
                                                        'numeric integer')),
                                (INTEGER_LONG, pgettext_lazy('DhcpOptionType',
                                                             'numeric long')),
                                (IPV4_X1, pgettext_lazy('DhcpOptionType',
                                                        'IPv4 * 1')),
                                (IPV4_X2, pgettext_lazy('DhcpOptionType',
                                                        'IPv4 * 2')),
                                (IPV4_MANY, pgettext_lazy('DhcpOptionType',
                                                          'IPv4 many')),
                            ),
                            verbose_name=pgettext_lazy(
                                'DhcpOptionType',
                                'type'))
    is_active = models.BooleanField(default=True,
                                    verbose_name=pgettext_lazy(
                                        'DhcpOptionType',
                                        'active'))

    # Set the managers for the model
    objects = models.Manager()
    objects_enabled = ManagerEnabled()
    objects_disabled = ManagerDisabled()

    class Meta:
        # Define the database table
        ordering = ['option', '-is_active', 'name']
        verbose_name = pgettext_lazy('DhcpOptionType',
                                     'DHCP option type')
        verbose_name_plural = pgettext_lazy('DhcpOptionType',
                                            'DHCP option types')

    def __str__(self):
        return '{OPTION} - {NAME}'.format(OPTION=self.option,
                                          NAME=self.name)

    def is_type_boolean(self):
        """
        Check if the option type is boolean
        """
        return self.type == self.BOOLEAN

    def is_type_character(self):
        """
        Check if the option type is character
        """
        return self.type == self.CHARACTER

    def is_type_numeric(self):
        """
        Check if the option type is numeric
        """
        return self.type in (self.INTEGER_SHORT,
                             self.INTEGER,
                             self.INTEGER_LONG)


class DhcpOptionTypeAdmin(BaseModelAdmin):
    pass
