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

from django.views.generic import ListView

from dnsmasq.models import Setting

from website.views.enabled_disabled_mixin import EnabledDisabledMixin
from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectListView(RequireLoginMixin,
                     EnabledDisabledMixin,
                     GenericMixin,
                     ListView):
    model = Setting
    template_name = 'website/settings/list.html'
    page_title = 'Settings'
    column_headers = [('Name', 'col-sm-3'),
                      ('Description', 'col-sm')]
