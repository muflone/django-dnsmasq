##
#     Project: Django website
# Description: A Django application to create website configuration
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

from django.urls import path

from website.views.dhcp_option_ipv4.create import DhcpOptionIpV4CreateView
from website.views.dhcp_option_ipv4.delete import DhcpOptionIpV4DeleteView
from website.views.dhcp_option_ipv4.detail import DhcpOptionIpV4DetailView
from website.views.dhcp_option_ipv4.list import DhcpOptionIpV4ListView


urlpatterns = []

# DHCP option IPv4 addresses create page
urlpatterns.append(path(route='create',
                        view=DhcpOptionIpV4CreateView.as_view(),
                        name='website.dhcp.option_ipv4.create'))
# DHCP option IPv4 addresses delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=DhcpOptionIpV4DeleteView.as_view(),
                        name='website.dhcp.option_ipv4.delete'))
# DHCP option IPv4 addresses detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=DhcpOptionIpV4DetailView.as_view(),
                        name='website.dhcp.option_ipv4.detail'))
# DHCP option IPv4 addresses list page
urlpatterns.append(path(route='list',
                        view=DhcpOptionIpV4ListView.as_view(),
                        name='website.dhcp.option_ipv4.list'))
