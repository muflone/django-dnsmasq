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

from dnsmasq.models import DhcpOption, DhcpTag

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class EasySetupDhcpDefaultOptionsView(RequireLoginMixin,
                                      GenericMixin,
                                      UpdateView):
    model = DhcpTag
    fields = ['name']
    success_url = reverse_lazy('website.easy_setup.dhcp_default_options')
    template_name = 'website/easy_setup/dhcp_default_options.html'
    page_title = 'DHCP default options'

    def get_object(self, queryset=None):
        """
        Get the record to update, if existing
        :return: DhcpTag with the default name
        """
        result = self.model.objects.filter(name=DhcpTag.DEFAULT_TAG).first()
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = DhcpOption.objects.filter(
            tag__name=DhcpTag.DEFAULT_TAG)
        return context

    def form_valid(self, form):
        """
        Save the DhcpTag object from the form
        """
        if not form.instance.pk:
            # Initialize data if the object doesn't exist
            form.instance.name = DhcpTag.DEFAULT_TAG
            form.instance.order = 0
        return super().form_valid(form)