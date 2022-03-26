##
#     Project: Django dnsmasq
# Description: A Django application to create dnsmasq configuration
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

from dnsmasq.constants import MODE_EASY_SETUP

from website.views.dhcp.tags.create import ObjectCreateView
from website.views.dhcp.tags.delete import ObjectDeleteView
from website.views.dhcp.tags.detail import ObjectDetailView
from website.views.dhcp.tags.disable import ObjectDisableView
from website.views.dhcp.tags.enable import ObjectEnableView
from website.views.dhcp.tags.list import ObjectListView


urlpatterns = []

# Easy Setup DHCP tags create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.easy_setup.dhcp.tags.create',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP tags delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.easy_setup.dhcp.tags.delete',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP tags detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.easy_setup.dhcp.tags.detail',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP tags disable page
urlpatterns.append(path(route='disable/<int:pk>',
                        view=ObjectDisableView.as_view(),
                        name='website.easy_setup.dhcp.tags.disable',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP tags enable page
urlpatterns.append(path(route='enable/<int:pk>',
                        view=ObjectEnableView.as_view(),
                        name='website.easy_setup.dhcp.tags.enable',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP tags list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.easy_setup.dhcp.tags.list',
                        kwargs={'mode': MODE_EASY_SETUP}))
