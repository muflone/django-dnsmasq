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


class Domain(BaseModel):
    """
    Domain names offered to hosts for obtaining their FQDN
    """
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name=pgettext_lazy(
                                'Domain',
                                'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'Domain',
                                       'description'))
    order = models.PositiveIntegerField(default=1,
                                        verbose_name=pgettext_lazy(
                                            'Domain',
                                            'order'))
    subnet_ip = models.GenericIPAddressField(blank=True,
                                             null=True,
                                             verbose_name=pgettext_lazy(
                                                 'Domain',
                                                 'subnet IP'))
    subnet_cidr = models.PositiveSmallIntegerField(default=0,
                                                   verbose_name=pgettext_lazy(
                                                       'Domain',
                                                       'subnet CIDR'))
    starting_ip = models.GenericIPAddressField(blank=True,
                                               null=True,
                                               verbose_name=pgettext_lazy(
                                                   'Domain',
                                                   'starting IP range'))
    ending_ip = models.GenericIPAddressField(blank=True,
                                             null=True,
                                             verbose_name=pgettext_lazy(
                                                 'Domain',
                                                 'ending IP range'))
    is_active = models.BooleanField(default=True,
                                    verbose_name=pgettext_lazy(
                                        'Domain',
                                        'active'))

    # Set the managers for the model
    objects = models.Manager()
    objects_enabled = ManagerEnabled()
    objects_disabled = ManagerDisabled()

    class Meta:
        # Define the database table
        ordering = ['order', '-is_active', 'name']
        verbose_name = pgettext_lazy('Domain',
                                     'Domain')
        verbose_name_plural = pgettext_lazy('Domain',
                                            'Domains')

    def __str__(self):
        return '{NAME}'.format(NAME=self.name)


class DomainAdmin(BaseModelAdmin):
    pass
