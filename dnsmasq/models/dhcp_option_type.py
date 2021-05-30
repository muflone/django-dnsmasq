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

from utility.models import BaseModel, BaseModelAdmin


class DhcpOptionType(BaseModel):
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
                                ('char', pgettext_lazy('DhcpOptionType',
                                                       'character')),
                                ('bool', pgettext_lazy('DhcpOptionType',
                                                       'boolean')),
                                ('int1', pgettext_lazy('DhcpOptionType',
                                                       'numeric byte')),
                                ('int2', pgettext_lazy('DhcpOptionType',
                                                       'numeric integer')),
                                ('int4', pgettext_lazy('DhcpOptionType',
                                                       'numeric long')),
                                ('ipv4x1', pgettext_lazy('DhcpOptionType',
                                                         'IPv4 * 1')),
                                ('ipv4x2', pgettext_lazy('DhcpOptionType',
                                                         'IPv4 * 2')),
                                ('ipv4', pgettext_lazy('DhcpOptionType',
                                                       'IPv4 many')),
                            ),
                            verbose_name=pgettext_lazy(
                                'DhcpOptionType',
                                'type'))
    status = models.BooleanField(default=True,
                                 verbose_name=pgettext_lazy(
                                     'DhcpOptionType',
                                     'status'))

    class Meta:
        # Define the database table
        ordering = ['option', 'name']
        verbose_name = pgettext_lazy('DhcpOptionType',
                                     'DHCP option type')
        verbose_name_plural = pgettext_lazy('DhcpOptionType',
                                            'DHCP option types')

    def __str__(self):
        return '{NAME}'.format(NAME=self.name)


class DhcpOptionTypeAdmin(BaseModelAdmin):
    pass