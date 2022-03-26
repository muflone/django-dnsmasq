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

from dnsmasq.constants import MODE_EASY_SETUP
from dnsmasq.models import DhcpOptionIpV4

from website.views.item_disable import ItemDisableView
from website.views.require_login import RequireLoginMixin


class ObjectDisableView(RequireLoginMixin,
                        ItemDisableView):
    model = DhcpOptionIpV4
    url = reverse_lazy('website.dhcp.option_ipv4.list')

    def get_redirect_url(self, *args, **kwargs):
        """
        Change redirect URL if the Easy Setup mode was requested
        """
        url = super().get_redirect_url(*args, **kwargs)
        if self.kwargs.get('mode') == MODE_EASY_SETUP:
            item = self.model.objects.get(pk=self.kwargs['pk'])
            url = reverse_lazy('website.easy_setup.dhcp.options.detail',
                               kwargs={'pk': item.option.pk})
        return url
