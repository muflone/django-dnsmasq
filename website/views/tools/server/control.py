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

from django.views.generic import TemplateView

from dnsmasq.constants import (SETTING_SERVER_SERVICE_NAME,
                               SETTING_SERVER_USE_SUDO)
from dnsmasq.misc.server import Server

from utility.misc.get_setting_value import get_setting_value

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ServerControlView(RequireLoginMixin,
                        GenericMixin,
                        TemplateView):
    template_name = 'website/tools/server/control.html'
    page_title = 'Server control'

    def get_context_data(self, **kwargs):
        """
        Get the context data
        """
        context = super().get_context_data(**kwargs)
        server = Server(
            name=get_setting_value(name=SETTING_SERVER_SERVICE_NAME),
            sudo=get_setting_value(name=SETTING_SERVER_USE_SUDO) == '1')
        context['is_active'] = server.is_active()
        return context
