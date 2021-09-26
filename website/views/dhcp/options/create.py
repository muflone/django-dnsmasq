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


class ObjectCreateView(RequireLoginMixin,
                       GenericMixin,
                       CreateView):
    model = DhcpOption
    fields = ['tag', 'option', 'description',
              'character_value', 'numeric_value', 'forced',
              'order', 'is_active']
    success_url = reverse_lazy('website.dhcp.options.list')
    template_name = 'website/dhcp/options/detail.html'
    page_title = 'Create new DHCP option'

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        # If the mode is passed set the current tag as disabled/fixed
        if 'tag' in self.kwargs:
            form = context['form']
            form.fields['tag'].widget.attrs['disabled'] = 'disabled'
            # Exclude options already present for the same tag_id
            options = DhcpOption.objects.filter(
                tag_id=DhcpTag.objects.filter(
                    pk=int(self.kwargs['tag'])).first())
            form.fields['option'].queryset = DhcpOptionType.objects.exclude(
                option__in=options.values_list('option__option', flat=True))
        return context

    def get_initial(self):
        initial = super().get_initial()
        # If the tag is passed set the current tag to the template
        if 'tag' in self.kwargs:
            tag = DhcpTag.objects.filter(pk=int(self.kwargs['tag'])).first()
            initial['tag'] = tag
        return initial

    def get_success_url(self):
        """
        Get the success URL to redirect after a successfull post.
        When the tag is passed redirect to the Easy Setup default options page
        """
        url = super().get_success_url()
        if self.kwargs.get('mode') == MODE_EASY_SETUP:
            url = (reverse_lazy('website.easy_setup.dhcp.default_options')
                   if int(self.kwargs['tag']) == DhcpTag.get_default().id
                   else reverse_lazy('website.easy_setup.dhcp.tags.detail',
                                     kwargs={'pk': self.kwargs['tag']}))
        return url
