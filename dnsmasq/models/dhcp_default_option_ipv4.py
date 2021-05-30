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

from django.contrib import admin
from django.db import models
from django.utils.translation import pgettext_lazy

from utility.models import BaseModel, BaseModelAdmin


class DhcpDefaultOptionIpV4(BaseModel):
    option = models.ForeignKey(to='DhcpDefaultOption',
                               verbose_name=pgettext_lazy(
                                   'DhcpDefaultOptionIpV4',
                                   'option'),
                               on_delete=models.PROTECT)
    address = models.GenericIPAddressField(protocol='ipv4',
                                           verbose_name=pgettext_lazy(
                                               'DhcpDefaultOptionIpV4',
                                               'address'))
    order = models.PositiveIntegerField(default=1,
                                        verbose_name=pgettext_lazy(
                                            'DhcpDefaultOptionIpV4',
                                            'order'))
    status = models.BooleanField(default=True,
                                 verbose_name=pgettext_lazy(
                                     'DhcpDefaultOption',
                                     'status'))

    class Meta:
        # Define the database table
        ordering = ['option', 'order']
        verbose_name = pgettext_lazy('DhcpDefaultOptionIpV4',
                                     'DHCP default option IPv4 address')
        verbose_name_plural = pgettext_lazy('DhcpDefaultOptionIpV4',
                                            'DHCP default options IPv4 '
                                            'addresses')

    def __str__(self):
        return '{NAME}'.format(NAME=self.option)


class DhcpDefaultOptionIpV4Admin(BaseModelAdmin):
    pass


class DhcpDefaultOptionIpV4InlineAdmin(admin.TabularInline):
    """
    Admin Inline to show children rows for DhcpDefaultOptionIpV4
    """
    model = DhcpDefaultOptionIpV4
    fields = ('address', 'order', 'status')
