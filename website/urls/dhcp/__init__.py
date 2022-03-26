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


# Hosts module
urlpatterns.append(path(route='hosts/',
                        view=include('website.urls.dhcp.hosts')))
# Option IPv4 module
urlpatterns.append(path(route='option_ipv4/',
                        view=include('website.urls.dhcp.option_ipv4')))
# Option Types module
urlpatterns.append(path(route='option_types/',
                        view=include('website.urls.dhcp.option_types')))
# Options module
urlpatterns.append(path(route='options/',
                        view=include('website.urls.dhcp.options')))
# Ranges module
urlpatterns.append(path(route='ranges/',
                        view=include('website.urls.dhcp.ranges')))
# Tags module
urlpatterns.append(path(route='tags/',
                        view=include('website.urls.dhcp.tags')))
