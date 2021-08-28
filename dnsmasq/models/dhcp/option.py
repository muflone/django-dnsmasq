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

from .option_ipv4 import DhcpOptionIpV4InlineAdmin

from utility.models import (BaseModel, BaseModelAdmin,
                            ManagerEnabled, ManagerDisabled)


class DhcpOption(BaseModel):
    """
    DHCP option with values
    """
    tag = models.ForeignKey(to='DhcpTag',
                            verbose_name=pgettext_lazy(
                                'DhcpOption',
                                'tag'),
                            on_delete=models.PROTECT)
    option = models.ForeignKey(to='DhcpOptionType',
                               verbose_name=pgettext_lazy(
                                   'DhcpOption',
                                   'option'),
                               on_delete=models.PROTECT)
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'DhcpOption',
                                       'description'))
    character_value = models.CharField(max_length=255,
                                       blank=True,
                                       null=True,
                                       verbose_name=pgettext_lazy(
                                           'DhcpOption',
                                           'character value'))
    numeric_value = models.IntegerField(blank=True,
                                        null=True,
                                        verbose_name=pgettext_lazy(
                                            'DhcpOption',
                                            'numeric value'))
    forced = models.BooleanField(default=False,
                                 verbose_name=pgettext_lazy(
                                     'DhcpOption',
                                     'forced'))
    is_active = models.BooleanField(default=True,
                                    verbose_name=pgettext_lazy(
                                        'DhcpOption',
                                        'active'))

    # Set the managers for the model
    objects = models.Manager()
    objects_enabled = ManagerEnabled()
    objects_disabled = ManagerDisabled()

    class Meta:
        # Define the database table
        ordering = ['tag', '-is_active', 'option__option']
        unique_together = [['tag', 'option']]
        verbose_name = pgettext_lazy('DhcpOption',
                                     'DHCP option')
        verbose_name_plural = pgettext_lazy('DhcpOption',
                                            'DHCP options')

    def __str__(self):
        return '{TAG} - {OPTION} - {NAME}'.format(TAG=self.tag,
                                                  OPTION=self.option.option,
                                                  NAME=self.option.name)


class DhcpOptionAdmin(BaseModelAdmin):
    pass


class DhcpOptionProxy(DhcpOption):
    class Meta:
        proxy = True
        verbose_name = pgettext_lazy('DhcpOption',
                                     'DHCP option (extended)')
        verbose_name_plural = pgettext_lazy('DhcpOption',
                                            'DHCP options (extended)')


class DhcpOptionProxyAdmin(BaseModelAdmin):
    inlines = [DhcpOptionIpV4InlineAdmin]
    list_per_page = 300
