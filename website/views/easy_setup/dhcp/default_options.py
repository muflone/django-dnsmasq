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

from dnsmasq.models import DhcpOption, DhcpTag

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class EasySetupDhcpDefaultOptionsView(RequireLoginMixin,
                                      GenericMixin,
                                      UpdateView):
    model = DhcpTag
    fields = ['name']
    success_url = reverse_lazy('website.easy_setup.dhcp.default_options')
    template_name = 'website/easy_setup/dhcp/default_options.html'
    page_title = 'DHCP default options'
    column_headers = [('Option', 'col-sm-3'),
                      ('Type', 'col-sm-2'),
                      ('Description', 'col-sm'),
                      ('Order', 'col-order')]

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        related = ['tag', 'option']
        context['object_enabled_list'] = DhcpOption.objects_enabled.filter(
            tag__name=DhcpTag.DEFAULT_TAG_NAME).select_related(*related)
        context['object_disabled_list'] = DhcpOption.objects_disabled.filter(
            tag__name=DhcpTag.DEFAULT_TAG_NAME).select_related(*related)
        context['DEFAULT_TAG_NAME'] = DhcpTag.DEFAULT_TAG_NAME
        return context

    def get_object(self, queryset=None):
        """
        Get the record to update, if existing
        :return: DhcpTag with the default name
        """
        result = self.model.objects.filter(
            name=DhcpTag.DEFAULT_TAG_NAME).first()
        return result

    def form_valid(self, form):
        """
        Save the DhcpTag object from the form
        """
        if not form.instance.pk:
            # Initialize data if the object doesn't exist
            form.instance.name = DhcpTag.DEFAULT_TAG_NAME
            form.instance.order = 0
        return super().form_valid(form)
