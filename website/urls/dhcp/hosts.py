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

from website.views.dhcp_hosts.create import ObjectCreateView
from website.views.dhcp_hosts.delete import ObjectDeleteView
from website.views.dhcp_hosts.detail import ObjectDetailView
from website.views.dhcp_hosts.list import ObjectListView


urlpatterns = []

# DHCP hosts create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.dhcp.hosts.create'))
# DHCP hosts delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.dhcp.hosts.delete'))
# DHCP hosts detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.dhcp.hosts.detail'))
# DHCP hosts list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.dhcp.hosts.list'))
