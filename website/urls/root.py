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
from django.views.generic import RedirectView

from website.views.dashboard import DashboardView

from website.views.auth.login import LoginView
from website.views.auth.logout import LogoutView


urlpatterns = []

# Home page
urlpatterns.append(path(route='',
                        view=DashboardView.as_view(),
                        name='website.home'))
# Login page
urlpatterns.append(path(route='login',
                        view=LoginView.as_view(),
                        name='website.auth.login'))
# Logout page
urlpatterns.append(path(route='logout',
                        view=LogoutView.as_view(),
                        name='website.auth.logout'))
# Favicon redirect
urlpatterns.append(path(route='favicon.ico',
                        view=RedirectView.as_view(
                            url='/static/website/img/favicon.ico',
                            permanent=True),
                        name='website.favicon'))
