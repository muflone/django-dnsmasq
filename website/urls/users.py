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

from website.views.users.create import ObjectCreateView
from website.views.users.delete import ObjectDeleteView
from website.views.users.detail import ObjectDetailView
from website.views.users.disable import ObjectDisableView
from website.views.users.enable import ObjectEnableView
from website.views.users.list import ObjectListView
from website.views.users.password import ObjectPasswordView


urlpatterns = []

# Users create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.users.create'))
# Users delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.users.delete'))
# Users detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.users.detail'))
# Users disable page
urlpatterns.append(path(route='disable/<int:pk>',
                        view=ObjectDisableView.as_view(),
                        name='website.users.disable'))
# Users enable page
urlpatterns.append(path(route='enable/<int:pk>',
                        view=ObjectEnableView.as_view(),
                        name='website.users.enable'))
# Users list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.users.list'))
# Users password set
urlpatterns.append(path(route='password/<int:pk>',
                        view=ObjectPasswordView.as_view(),
                        name='website.users.password'))
