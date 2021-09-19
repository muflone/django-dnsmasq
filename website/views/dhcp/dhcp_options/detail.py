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

from django.urls import reverse_lazy
from django.views.generic import UpdateView

from dnsmasq.constants import MODE_EASY_SETUP
from dnsmasq.models import DhcpOption

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectDetailView(RequireLoginMixin,
                       GenericMixin,
                       UpdateView):
    model = DhcpOption
    fields = ['tag', 'option', 'description',
              'character_value', 'numeric_value', 'forced', 'order',
              'is_active']
    success_url = reverse_lazy('website.dhcp.options.list')
    template_name = 'website/dhcp/options/detail.html'
    page_title = 'DHCP option detail'

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        # If the mode is passed set it as disabled/fixed
        if 'mode' in self.kwargs:
            form = context['form']
            form.fields['tag'].widget.attrs['disabled'] = 'disabled'
            # If the object has an option set set the field as disabled/fixed
            if self.object.option:
                form.fields['option'].widget.attrs['disabled'] = 'disabled'
        return context

    def get_initial(self):
        initial = super().get_initial()
        # If the mode is passed set the current object Tag as default
        if 'mode' in self.kwargs:
            initial['tag'] = self.object.tag
        return initial

    def get_success_url(self):
        """
        Get the success URL to redirect after a successfull post.
        When the tag is passed redirect to the Easy Setup default options page
        """
        url = super().get_success_url()
        if self.kwargs.get('mode', None) == MODE_EASY_SETUP:
            url = reverse_lazy('website.easy_setup.dhcp.default_options')
        return url
