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

from macaddress.fields import MACAddressField

from utility.models import BaseModel, BaseModelAdmin, ManagerEnabled


class DhcpHost(BaseModel):
    """
    DHCP host configuration
    """
    name = models.CharField(max_length=255,
                            verbose_name=pgettext_lazy(
                                'DhcpHost',
                                'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'DhcpHost',
                                       'description'))
    mac_address = MACAddressField(integer=True,
                                  blank=False,
                                  null=False,
                                  unique=True,
                                  verbose_name=pgettext_lazy(
                                      'DhcpHost',
                                      'mac address'))
    address = models.GenericIPAddressField(protocol='ipv4',
                                           blank=True,
                                           null=True,
                                           verbose_name=pgettext_lazy(
                                               'DhcpHost',
                                               'address'))
    tag = models.ForeignKey(to='DhcpTag',
                            null=True,
                            blank=True,
                            verbose_name=pgettext_lazy(
                                'DhcpHost',
                                'options tag'),
                            on_delete=models.PROTECT)
    ignored = models.BooleanField(default=False,
                                  verbose_name=pgettext_lazy(
                                      'DhcpHost',
                                      'ignored'))
    status = models.BooleanField(default=True,
                                 verbose_name=pgettext_lazy(
                                     'DhcpHost',
                                     'status'))

    # Set the managers for the model
    objects = models.Manager()
    objects_enabled = ManagerEnabled()

    class Meta:
        # Define the database table
        ordering = ['name']
        verbose_name = pgettext_lazy('DhcpHost',
                                     'DHCP host')
        verbose_name_plural = pgettext_lazy('DhcpHost',
                                            'DHCP hosts')

    def __str__(self):
        return '{NAME}'.format(NAME=self.name)


class DhcpHostAdmin(BaseModelAdmin):
    pass
