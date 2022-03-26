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

from dnsmasq.constants import MODE_EASY_SETUP

from website.views.easy_setup.dhcp.default_options import (
    EasySetupDhcpDefaultOptionsView)
from website.views.easy_setup.dhcp.default_policy import (
    EasySetupDhcpDefaultPolicyView)


urlpatterns = []

# Easy Setup DHCP default options
urlpatterns.append(path(route='default_options',
                        view=EasySetupDhcpDefaultOptionsView.as_view(),
                        name='website.easy_setup.dhcp.default_options',
                        kwargs={'mode': MODE_EASY_SETUP}))
# Easy Setup DHCP default policy
urlpatterns.append(path(route='default_policy',
                        view=EasySetupDhcpDefaultPolicyView.as_view(),
                        name='website.easy_setup.dhcp.default_policy',
                        kwargs={'mode': MODE_EASY_SETUP}))
