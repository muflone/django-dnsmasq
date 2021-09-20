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

from django.views.generic import ListView

from dnsmasq.constants import SETTING_LEASES_PATH

from utility.misc.get_setting_value import get_setting_value
from utility.models.lease import Lease

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectListView(RequireLoginMixin,
                     GenericMixin,
                     ListView):
    template_name = 'website/tools/leases/list.html'
    page_title = 'Leases'
    column_headers = [('Address', 'col-sm-3'),
                      ('MAC address', 'col-leases-mac_address'),
                      ('Expiration', 'col-leases-expiration-date'),
                      ('', 'col-leases-expiration'),
                      ('Description', 'col-sm')]

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        context['object_enabled_list'] = self.object_list
        return context

    def get_queryset(self):
        """
        Get the leases list, sorting results by numeric address
        :return:
        """
        results = []
        if configuration_path := get_setting_value(name=SETTING_LEASES_PATH):
            # Load the leases
            with open(configuration_path, 'r') as file:
                for line in file:
                    results.append(Lease.load_from_string(line))
        return sorted(results, key=lambda item: item.address_numeric)
