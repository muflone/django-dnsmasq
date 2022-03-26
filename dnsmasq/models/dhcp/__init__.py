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

from .host import DhcpHost, DhcpHostAdmin                          # noqa: F401
from .option import (DhcpOption,                                   # noqa: F401
                     DhcpOptionAdmin,                              # noqa: F401
                     DhcpOptionProxy,                              # noqa: F401
                     DhcpOptionProxyAdmin)                         # noqa: F401
from .option_ipv4 import DhcpOptionIpV4, DhcpOptionIpV4Admin       # noqa: F401
from .option_type import DhcpOptionType, DhcpOptionTypeAdmin       # noqa: F401
from .range import DhcpRange, DhcpRangeAdmin                       # noqa: F401
from .tag import DhcpTag, DhcpTagAdmin                             # noqa: F401
