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
from django.views.generic import CreateView

from dnsmasq.constants import MODE_EASY_SETUP
from dnsmasq.models import DhcpOption, DhcpOptionType, DhcpTag

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class DhcpOptionsCreateView(RequireLoginMixin,
                            GenericMixin,
                            CreateView):
    model = DhcpOption
    fields = ['tag', 'option', 'description',
              'character_value', 'numeric_value', 'forced',
              'order', 'is_active']
    template_name = 'website/dhcp_options/detail.html'
    page_title = 'Create new DHCP option'

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        # If the mode is passed set the current tag as disabled/fixed
        if 'mode' in self.kwargs:
            form = context['form']
            form.fields['tag'].widget.attrs['disabled'] = 'disabled'
            # Exclude options already present for the same tag_id
            options = DhcpOption.objects.filter(
                tag_id=DhcpTag.get_default().id)
            form.fields['option'].queryset = DhcpOptionType.objects.exclude(
                option__in=options.values_list('option__option', flat=True))
        return context

    def get_initial(self):
        initial = super().get_initial()
        # If the mode is passed set the current tag as default
        if 'mode' in self.kwargs:
            initial['tag'] = DhcpTag.get_default()
        return initial

    def get_success_url(self):
        """
        Get the success URL to redirect after a successfull post.
        When the tag is passed redirect to the Easy Setup default options page
        """
        success_url = reverse_lazy(
            'website.easy_setup.dhcp.default_options'
            if self.kwargs.get('mode', None) == MODE_EASY_SETUP
            else 'website.dhcp.options.list')
        return success_url
