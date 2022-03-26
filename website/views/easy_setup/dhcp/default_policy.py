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
from django.views.generic import UpdateView

from dnsmasq.models import DhcpHost

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class EasySetupDhcpDefaultPolicyView(RequireLoginMixin,
                                     GenericMixin,
                                     UpdateView):
    model = DhcpHost
    fields = ['name', 'ignored', 'is_active']
    success_url = reverse_lazy('website.easy_setup.dhcp.default_policy')
    template_name = 'website/easy_setup/dhcp/default_policy.html'
    page_title = 'DHCP default policy'

    def get_object(self, queryset=None):
        """
        Get the record to update, if existing
        :return: DhcpHost with the MAC address with zeros
        """
        result = self.model.objects.filter(
            mac_address=DhcpHost.MAC_ADDRESS_ZERO).first()
        return result

    def form_valid(self, form):
        """
        Save the DhcpHost object from the form
        """
        if not form.instance.pk:
            # Initialize data if the object doesn't exist
            form.instance.mac_address = DhcpHost.MAC_ADDRESS_ZERO
            form.instance.order = 0
        return super().form_valid(form)
