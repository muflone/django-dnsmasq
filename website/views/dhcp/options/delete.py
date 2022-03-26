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
from django.views.generic import DeleteView

from dnsmasq.constants import MODE_EASY_SETUP
from dnsmasq.models import DhcpOption, DhcpTag

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectDeleteView(RequireLoginMixin,
                       GenericMixin,
                       DeleteView):
    model = DhcpOption
    success_url = reverse_lazy('website.dhcp.options.list')
    template_name = 'website/dhcp/options/delete.html'
    page_title = 'DHCP option deletion'

    def get_success_url(self):
        """
        Get the success URL to redirect after a successfull post.
        When the tag is passed redirect to the Easy Setup default options page
        """
        url = super().get_success_url()
        if self.kwargs.get('mode') == MODE_EASY_SETUP:
            url = (reverse_lazy('website.easy_setup.dhcp.default_options')
                   if self.object.tag.name == DhcpTag.DEFAULT_TAG_NAME
                   else reverse_lazy('website.easy_setup.dhcp.tags.detail',
                                     kwargs={'pk': self.object.tag_id}))
        return url
