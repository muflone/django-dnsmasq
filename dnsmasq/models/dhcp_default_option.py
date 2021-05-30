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

from .dhcp_default_option_ipv4 import DhcpDefaultOptionIpV4InlineAdmin

from utility.models import BaseModel, BaseModelAdmin


class DhcpDefaultOption(BaseModel):
    option = models.ForeignKey(to='DhcpOptionType',
                               verbose_name=pgettext_lazy(
                                   'DhcpDefaultOption',
                                   'option'),
                               on_delete=models.PROTECT)
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'DhcpDefaultOption',
                                       'description'))
    character_value = models.CharField(max_length=255,
                                       blank=True,
                                       null=True,
                                       verbose_name=pgettext_lazy(
                                           'DhcpDefaultOption',
                                           'character value'))
    numeric_value = models.IntegerField(blank=True,
                                        null=True,
                                        verbose_name=pgettext_lazy(
                                            'DhcpDefaultOption',
                                            'numeric value'))
    status = models.BooleanField(default=True,
                                 verbose_name=pgettext_lazy(
                                     'DhcpDefaultOption',
                                     'status'))

    class Meta:
        # Define the database table
        ordering = ['option__option']
        verbose_name = pgettext_lazy('DhcpDefaultOption',
                                     'DHCP default option')
        verbose_name_plural = pgettext_lazy('DhcpDefaultOption',
                                            'DHCP default options')

    def __str__(self):
        return '{NAME}'.format(NAME=self.option.name)


class DhcpDefaultOptionAdmin(BaseModelAdmin):
    pass


class DhcpDefaultOptionProxy(DhcpDefaultOption):
    class Meta:
        proxy = True
        verbose_name = pgettext_lazy('DhcpDefaultOption',
                                     'DHCP default option (extended)')
        verbose_name_plural = pgettext_lazy('DhcpDefaultOption',
                                            'DHCP default options (extended)')


class DhcpDefaultOptionProxyAdmin(BaseModelAdmin):
    inlines = [DhcpDefaultOptionIpV4InlineAdmin]
    list_per_page = 300
