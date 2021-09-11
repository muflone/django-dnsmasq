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

from website.views.dhcp_options.create import DhcpOptionsCreateView
from website.views.dhcp_options.delete import DhcpOptionsDeleteView
from website.views.dhcp_options.detail import DhcpOptionsDetailView
from website.views.dhcp_options.list import DhcpOptionsListView


urlpatterns = []

# DHCP options create page
urlpatterns.append(path(route='create',
                        view=DhcpOptionsCreateView.as_view(),
                        name='website.dhcp.options.create'))
# DHCP options delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=DhcpOptionsDeleteView.as_view(),
                        name='website.dhcp.options.delete'))
# DHCP options detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=DhcpOptionsDetailView.as_view(),
                        name='website.dhcp.options.detail'))
# DHCP options list page
urlpatterns.append(path(route='list',
                        view=DhcpOptionsListView.as_view(),
                        name='website.dhcp.options.list'))
