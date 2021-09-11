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

from django.urls import include, path


urlpatterns = []

# Root module
urlpatterns.append(path(route='',
                        view=include('website.urls.root')))
# Configuration module
urlpatterns.append(path(route='configuration/',
                        view=include('website.urls.configuration')))
# DHCP module
urlpatterns.append(path(route='dhcp/',
                        view=include('website.urls.dhcp')))
# Domains module
urlpatterns.append(path(route='domains/',
                        view=include('website.urls.domains')))
# Easy Setup module
urlpatterns.append(path(route='easy_setup/',
                        view=include('website.urls.easy_setup')))
# Interfaces module
urlpatterns.append(path(route='interfaces/',
                        view=include('website.urls.interfaces')))
# Listening Addresses module
urlpatterns.append(path(route='listen_addresses/',
                        view=include('website.urls.listen_addresses')))
# Options module
urlpatterns.append(path(route='options/',
                        view=include('website.urls.options')))
# Settings module
urlpatterns.append(path(route='settings/',
                        view=include('website.urls.settings')))
# Users module
urlpatterns.append(path(route='users/',
                        view=include('website.urls.users')))
