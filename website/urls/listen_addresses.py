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

from django.urls import path

from website.views.listen_addresses.create import ObjectCreateView
from website.views.listen_addresses.delete import ObjectDeleteView
from website.views.listen_addresses.detail import ObjectDetailView
from website.views.listen_addresses.disable import ObjectDisableView
from website.views.listen_addresses.enable import ObjectEnableView
from website.views.listen_addresses.list import ObjectListView


urlpatterns = []

# Listening addresses create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.listen_addresses.create'))
# Listening addresses delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.listen_addresses.delete'))
# Listening addresses detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.listen_addresses.detail'))
# Listening addresses disable page
urlpatterns.append(path(route='disable/<int:pk>',
                        view=ObjectDisableView.as_view(),
                        name='website.listen_addresses.disable'))
# Listening addresses enable page
urlpatterns.append(path(route='enable/<int:pk>',
                        view=ObjectEnableView.as_view(),
                        name='website.listen_addresses.enable'))
# Listening addresses list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.listen_addresses.list'))
