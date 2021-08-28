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

from dnsmasq.models import (DhcpHost,
                            DhcpOption,
                            DhcpOptionIpV4,
                            DhcpOptionType,
                            DhcpRange,
                            DhcpTag,
                            Domain,
                            Interface,
                            ListenAddress,
                            Option,
                            Setting)

from utility.misc import group_by_is_active

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class DashboardView(RequireLoginMixin,
                    GenericMixin,
                    TemplateView):
    template_name = 'website/dashboard/dashboard.html'
    page_title = 'Dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = group_by_is_active(User)
        context['dhcp_hosts'] = group_by_is_active(DhcpHost)
        context['dhcp_options'] = group_by_is_active(DhcpOption)
        context['dhcp_option_ipv4'] = group_by_is_active(DhcpOptionIpV4)
        context['dhcp_option_types'] = group_by_is_active(DhcpOptionType)
        context['dhcp_ranges'] = group_by_is_active(DhcpRange)
        context['dhcp_tags'] = group_by_is_active(DhcpTag)
        context['domains'] = group_by_is_active(Domain)
        context['interfaces'] = group_by_is_active(Interface)
        context['listen_addresses'] = group_by_is_active(ListenAddress)
        context['options'] = group_by_is_active(Option)
        context['settings'] = group_by_is_active(Setting)
        return context
