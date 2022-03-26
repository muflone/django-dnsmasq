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

from dnsmasq.models import DhcpHost

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectListView(RequireLoginMixin,
                     GenericMixin,
                     ListView):
    model = DhcpHost
    template_name = 'website/dhcp/hosts/list.html'
    page_title = 'DHCP hosts'
    column_headers = [('Name', 'col-sm-3'),
                      ('MAC address', 'col-sm-10-percent'),
                      ('IP address', 'col-sm-10-percent'),
                      ('Tag', 'col-sm-2'),
                      ('Description', 'col-sm'),
                      ('Order', 'col-order')]

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        context['MAC_ADDRESS_ZERO'] = DhcpHost.MAC_ADDRESS_ZERO
        # Add objects_enabled using ObjectsEnabled
        queryset = self.model.objects_enabled.all()
        # If the mode is passed hide the default host
        if 'mode' in self.kwargs:
            queryset = queryset.exclude(mac_address=DhcpHost.MAC_ADDRESS_ZERO)
        related = ['tag']
        context['object_enabled_list'] = queryset.select_related(*related)
        # If the mode is passed hide the default host
        queryset = self.model.objects_disabled.all()
        if 'mode' in self.kwargs:
            queryset = queryset.exclude(mac_address=DhcpHost.MAC_ADDRESS_ZERO)
        context['object_disabled_list'] = queryset.select_related(*related)
        return context
