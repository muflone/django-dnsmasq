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

from django.urls import include, path


urlpatterns = []


# Root module
urlpatterns.append(path(
    route='',
    view=include('website.urls.easy_setup.dhcp.root')))
# Hosts module
urlpatterns.append(path(
    route='hosts/',
    view=include('website.urls.easy_setup.dhcp.hosts')))
# Option IPv4 module
urlpatterns.append(path(
    route='option_ipv4/',
    view=include('website.urls.easy_setup.dhcp.option_ipv4')))
# Options module
urlpatterns.append(path(
    route='options/',
    view=include('website.urls.easy_setup.dhcp.options')))
# Options module
urlpatterns.append(path(
    route='tags/',
    view=include('website.urls.easy_setup.dhcp.tags')))
