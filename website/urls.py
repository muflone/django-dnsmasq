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

from website.views.home import HomeView

from website.views.auth.login import LoginView
from website.views.auth.logout import LogoutView

from website.views.users.create import UsersCreateView
from website.views.users.delete import UsersDeleteView
from website.views.users.detail import UsersDetailView
from website.views.users.list import UsersListView


urlpatterns = []
# Login page
urlpatterns.append(path(route='login',
                        view=LoginView.as_view(),
                        name='website.auth.login'))
# Logout page
urlpatterns.append(path(route='logout',
                        view=LogoutView.as_view(),
                        name='website.auth.logout'))
# Home page
urlpatterns.append(path(route='',
                        view=HomeView.as_view(),
                        name='website.home'))
# Users list page
urlpatterns.append(path(route='users/list',
                        view=UsersListView.as_view(),
                        name='website.users.list'))
# Users detail page
urlpatterns.append(path(route='users/<int:pk>',
                        view=UsersDetailView.as_view(),
                        name='website.users.detail'))
# Users delete page
urlpatterns.append(path(route='users/delete/<int:pk>',
                        view=UsersDeleteView.as_view(),
                        name='website.users.delete'))
# Users create page
urlpatterns.append(path(route='users/create',
                        view=UsersCreateView.as_view(),
                        name='website.users.create'))
