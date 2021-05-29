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


class Interface(BaseModel):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name=pgettext_lazy(
                                'Interface',
                                'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'Interface',
                                       'description'))
    order = models.PositiveIntegerField(default=1,
                                        verbose_name=pgettext_lazy(
                                            'Interface',
                                            'order'))
    excluded = models.BooleanField(default=False,
                                   verbose_name=pgettext_lazy(
                                       'Interface',
                                       'excluded'))
    disable_dhcp = models.BooleanField(default=False,
                                       verbose_name=pgettext_lazy(
                                           'Interface',
                                           'disable for DHCP'))
    status = models.BooleanField(default=True,
                                 verbose_name=pgettext_lazy(
                                     'Interface',
                                     'status'))

    class Meta:
        # Define the database table
        ordering = ['order', 'name']
        verbose_name = pgettext_lazy('Interface',
                                     'Interface')
        verbose_name_plural = pgettext_lazy('Interface',
                                            'Interfaces')

    def __str__(self):
        return '{NAME}'.format(NAME=self.name)


class InterfaceAdmin(BaseModelAdmin):
    pass
