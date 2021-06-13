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


class DhcpTag(BaseModel):
    """
    DHCP Tag for grouping options
    """
    name = models.SlugField(max_length=255,
                            unique=True,
                            verbose_name=pgettext_lazy(
                                'DhcpTag',
                                'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy(
                                       'DhcpTag',
                                       'description'))

    class Meta:
        # Define the database table
        ordering = ['name']
        verbose_name = pgettext_lazy('DhcpTag',
                                     'DHCP tag')
        verbose_name_plural = pgettext_lazy('DhcpTag',
                                            'DHCP tags')

    def __str__(self):
        return '{NAME}'.format(NAME=self.name)


class DhcpTagAdmin(BaseModelAdmin):
    pass
