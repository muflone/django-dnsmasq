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

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from dnsmasq.models import DhcpOptionIpV4

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectDeleteView(RequireLoginMixin,
                       GenericMixin,
                       DeleteView):
    model = DhcpOptionIpV4
    success_url = reverse_lazy('website.dhcp.option_ipv4.list')
    template_name = 'website/dhcp_option_ipv4/delete.html'
    page_title = 'DHCP option IPv4 address deletion'
