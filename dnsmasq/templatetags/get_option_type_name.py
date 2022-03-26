##
#     Project: Django dnsmasq
# Description: A Django application to create dnsmasq configuration
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2021-2022 Fabio Castelli
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

from django import template
from django.utils.translation import pgettext_lazy

from dnsmasq.models.dhcp import DhcpOptionType


register = template.Library()


@register.filter
def get_option_type_name(dhcp_option_type_key: str) -> str:
    """
    Custom filter to get the translated option type
    :param dhcp_option_type_key: option type name
    :return: translated option type name
    """
    return DhcpOptionType.NAMES.get(dhcp_option_type_key,
                                    pgettext_lazy('DhcpOptionType', 'Unknown'))
