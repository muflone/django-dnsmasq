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

from dnsmasq.constants import MODE_EASY_SETUP

from website.views.dhcp_option_ipv4.create import ObjectCreateView
from website.views.dhcp_option_ipv4.detail import ObjectDetailView
from website.views.dhcp_option_ipv4.disable import ObjectDisableView
from website.views.dhcp_option_ipv4.enable import ObjectEnableView


urlpatterns = []

# Easy Setup DHCP options create page
urlpatterns.append(path(route='create/<int:pk>',
                        view=ObjectCreateView.as_view(),
                        name='website.easy_setup.dhcp.option_ipv4.create',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP options detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.easy_setup.dhcp.option_ipv4.detail',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP options disable page
urlpatterns.append(path(route='disable/<int:pk>',
                        view=ObjectDisableView.as_view(),
                        name='website.easy_setup.dhcp.option_ipv4.disable',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP options enable page
urlpatterns.append(path(route='enable/<int:pk>',
                        view=ObjectEnableView.as_view(),
                        name='website.easy_setup.dhcp.option_ipv4.enable',
                        kwargs={'mode': MODE_EASY_SETUP}))
