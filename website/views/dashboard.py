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

from django.contrib.auth.models import User
from django.views.generic import TemplateView

from dnsmasq.models import (Action,
                            DhcpHost,
                            DhcpOption,
                            DhcpOptionIpV4,
                            DhcpOptionType,
                            DhcpRange,
                            DhcpTag,
                            Domain,
                            Interface,
                            ListenAddress,
                            Option)

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class DashboardView(RequireLoginMixin,
                    GenericMixin,
                    TemplateView):
    template_name = 'website/dashboard.html'
    page_title = 'Dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['actions'] = Action.objects.all()
        context['dhcp_hosts'] = DhcpHost.objects.all()
        context['dhcp_options'] = DhcpOption.objects.all()
        context['dhcp_option_ipv4'] = DhcpOptionIpV4.objects.all()
        context['dhcp_option_types'] = DhcpOptionType.objects.all()
        context['dhcp_ranges'] = DhcpRange.objects.all()
        context['dhcp_tags'] = DhcpTag.objects.all()
        context['domains'] = Domain.objects.all()
        context['interfaces'] = Interface.objects.all()
        context['listen_addresses'] = ListenAddress.objects.all()
        context['options'] = Option.objects.all()
        return context
