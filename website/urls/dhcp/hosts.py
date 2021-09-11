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

from website.views.dhcp_hosts.create import DhcpHostsCreateView
from website.views.dhcp_hosts.delete import DhcpHostsDeleteView
from website.views.dhcp_hosts.detail import DhcpHostsDetailView
from website.views.dhcp_hosts.list import DhcpHostsListView


urlpatterns = []

# DHCP hosts create page
urlpatterns.append(path(route='create',
                        view=DhcpHostsCreateView.as_view(),
                        name='website.dhcp.hosts.create'))
# DHCP hosts delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=DhcpHostsDeleteView.as_view(),
                        name='website.dhcp.hosts.delete'))
# DHCP hosts detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=DhcpHostsDetailView.as_view(),
                        name='website.dhcp.hosts.detail'))
# DHCP hosts list page
urlpatterns.append(path(route='list',
                        view=DhcpHostsListView.as_view(),
                        name='website.dhcp.hosts.list'))
