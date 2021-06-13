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

from django.contrib import admin

from .models import (Action, ActionAdmin,
                     DhcpDefaultOption, DhcpDefaultOptionAdmin,
                     DhcpDefaultOptionProxy, DhcpDefaultOptionProxyAdmin,
                     DhcpDefaultOptionIpV4, DhcpDefaultOptionIpV4Admin,
                     DhcpHost, DhcpHostAdmin,
                     DhcpOptionType, DhcpOptionTypeAdmin,
                     DhcpRange, DhcpRangeAdmin,
                     DhcpTag, DhcpTagAdmin,
                     Domain, DomainAdmin,
                     Interface, InterfaceAdmin,
                     ListenAddress, ListenAddressAdmin,
                     Option, OptionAdmin)


admin.site.register(Action, ActionAdmin)
admin.site.register(DhcpDefaultOption, DhcpDefaultOptionAdmin)
admin.site.register(DhcpDefaultOptionProxy, DhcpDefaultOptionProxyAdmin)
admin.site.register(DhcpDefaultOptionIpV4, DhcpDefaultOptionIpV4Admin)
admin.site.register(DhcpHost, DhcpHostAdmin)
admin.site.register(DhcpOptionType, DhcpOptionTypeAdmin)
admin.site.register(DhcpRange, DhcpRangeAdmin)
admin.site.register(DhcpTag, DhcpTagAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(ListenAddress, ListenAddressAdmin)
admin.site.register(Option, OptionAdmin)
