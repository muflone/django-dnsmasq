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

import fileinput

from django.urls import reverse_lazy
from django.views.generic import RedirectView

from dnsmasq.constants import SETTING_LEASES_PATH

from utility.misc.get_setting_value import get_setting_value
from utility.models.lease import Lease

from website.views.require_login import RequireLoginMixin


class ObjectDeleteView(RequireLoginMixin,
                       RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        address = self.kwargs['address']
        mac_address = self.kwargs['mac_address']
        if configuration_path := get_setting_value(name=SETTING_LEASES_PATH):
            # Filter out the leases
            with fileinput.FileInput(configuration_path,
                                     inplace=True) as file:
                for line in file:
                    lease = Lease.load_from_string(line)
                    if (lease.address != address or
                            lease.mac_address != mac_address):
                        # Inlude only the lines which don't match
                        print(line, end='')
        return reverse_lazy('website.tools.leases.list')
