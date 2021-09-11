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

from website.views.listen_addresses.create import ListenAddressesCreateView
from website.views.listen_addresses.delete import ListenAddressesDeleteView
from website.views.listen_addresses.detail import ListenAddressesDetailView
from website.views.listen_addresses.list import ListenAddressesListView


urlpatterns = []

# Listening addresses create page
urlpatterns.append(path(route='create',
                        view=ListenAddressesCreateView.as_view(),
                        name='website.listen_addresses.create'))
# Listening addresses delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ListenAddressesDeleteView.as_view(),
                        name='website.listen_addresses.delete'))
# Listening addresses detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ListenAddressesDetailView.as_view(),
                        name='website.listen_addresses.detail'))
# Listening addresses list page
urlpatterns.append(path(route='list',
                        view=ListenAddressesListView.as_view(),
                        name='website.listen_addresses.list'))
