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

from website.views.actions.create import ActionsCreateView
from website.views.actions.delete import ActionsDeleteView
from website.views.actions.detail import ActionsDetailView
from website.views.actions.list import ActionsListView

from website.views.options.create import OptionsCreateView
from website.views.options.delete import OptionsDeleteView
from website.views.options.detail import OptionsDetailView
from website.views.options.list import OptionsListView

from website.views.users.create import UsersCreateView
from website.views.users.delete import UsersDeleteView
from website.views.users.detail import UsersDetailView
from website.views.users.list import UsersListView
from website.views.users.password import UsersPasswordView


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
# Users password set
urlpatterns.append(path(route='users/password/<int:pk>',
                        view=UsersPasswordView.as_view(),
                        name='website.users.password'))

# Actions list page
urlpatterns.append(path(route='actions/list',
                        view=ActionsListView.as_view(),
                        name='website.actions.list'))
# Actions detail page
urlpatterns.append(path(route='actions/detail/<int:pk>',
                        view=ActionsDetailView.as_view(),
                        name='website.actions.detail'))
# Actions delete page
urlpatterns.append(path(route='actions/delete/<int:pk>',
                        view=ActionsDeleteView.as_view(),
                        name='website.actions.delete'))
# Actions create page
urlpatterns.append(path(route='actions/create',
                        view=ActionsCreateView.as_view(),
                        name='website.actions.create'))

# Options list page
urlpatterns.append(path(route='options/list',
                        view=OptionsListView.as_view(),
                        name='website.options.list'))
# Options detail page
urlpatterns.append(path(route='options/detail/<int:pk>',
                        view=OptionsDetailView.as_view(),
                        name='website.options.detail'))
# Options delete page
urlpatterns.append(path(route='options/delete/<int:pk>',
                        view=OptionsDeleteView.as_view(),
                        name='website.options.delete'))
# Options create page
urlpatterns.append(path(route='options/create',
                        view=OptionsCreateView.as_view(),
                        name='website.options.create'))
