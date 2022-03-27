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

from website.views.tools.server.control import ServerControlView
from website.views.tools.server.restart import ServerRestartView
from website.views.tools.server.start import ServerStartView
from website.views.tools.server.stop import ServerStopView


urlpatterns = []

# Server control page
urlpatterns.append(path(route='control',
                        view=ServerControlView.as_view(),
                        name='website.tools.server.control'))
# Server restart page
urlpatterns.append(path(route='restart',
                        view=ServerRestartView.as_view(),
                        name='website.tools.server.restart'))
# Server start page
urlpatterns.append(path(route='start',
                        view=ServerStartView.as_view(),
                        name='website.tools.server.start'))
# Server stop page
urlpatterns.append(path(route='stop',
                        view=ServerStopView.as_view(),
                        name='website.tools.server.stop'))
