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

from website.views.dhcp_tags.create import DhcpTagsCreateView
from website.views.dhcp_tags.delete import DhcpTagsDeleteView
from website.views.dhcp_tags.detail import DhcpTagsDetailView
from website.views.dhcp_tags.list import DhcpTagsListView


urlpatterns = []

# DHCP tags create page
urlpatterns.append(path(route='create',
                        view=DhcpTagsCreateView.as_view(),
                        name='website.dhcp.tags.create'))
# DHCP tags delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=DhcpTagsDeleteView.as_view(),
                        name='website.dhcp.tags.delete'))
# DHCP tags detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=DhcpTagsDetailView.as_view(),
                        name='website.dhcp.tags.detail'))
# DHCP tags list page
urlpatterns.append(path(route='list',
                        view=DhcpTagsListView.as_view(),
                        name='website.dhcp.tags.list'))
