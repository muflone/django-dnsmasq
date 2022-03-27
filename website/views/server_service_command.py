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

from django.urls import reverse_lazy
from django.views.generic import RedirectView

from dnsmasq.constants import (SETTING_SERVER_SERVICE_NAME,
                               SETTING_SERVER_USE_SUDO)
from dnsmasq.misc.server import Server

from utility.misc.get_setting_value import get_setting_value

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ServerServiceCommandView(RequireLoginMixin,
                               GenericMixin,
                               RedirectView):
    """
    Execute a service command
    """

    def get_server(self) -> Server:
        """
        Get a server object to execute service commands
        :return: Server instance
        """
        return Server(
            name=get_setting_value(name=SETTING_SERVER_SERVICE_NAME),
            sudo=get_setting_value(name=SETTING_SERVER_USE_SUDO) == '1')

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('website.tools.server.control')
