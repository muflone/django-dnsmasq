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

from website.views.users.create import UsersCreateView
from website.views.users.delete import UsersDeleteView
from website.views.users.detail import UsersDetailView
from website.views.users.list import UsersListView
from website.views.users.password import UsersPasswordView


urlpatterns = []

# Users create page
urlpatterns.append(path(route='create',
                        view=UsersCreateView.as_view(),
                        name='website.users.create'))
# Users delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=UsersDeleteView.as_view(),
                        name='website.users.delete'))
# Users detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=UsersDetailView.as_view(),
                        name='website.users.detail'))
# Users list page
urlpatterns.append(path(route='list',
                        view=UsersListView.as_view(),
                        name='website.users.list'))
# Users password set
urlpatterns.append(path(route='password/<int:pk>',
                        view=UsersPasswordView.as_view(),
                        name='website.users.password'))
