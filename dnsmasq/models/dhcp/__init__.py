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

from .default_option import (DhcpDefaultOption,                    # noqa: F401
                             DhcpDefaultOptionAdmin,               # noqa: F401
                             DhcpDefaultOptionProxy,               # noqa: F401
                             DhcpDefaultOptionProxyAdmin)          # noqa: F401
from .default_option_ipv4 import (DhcpDefaultOptionIpV4,           # noqa: F401
                                  DhcpDefaultOptionIpV4Admin)      # noqa: F401
from .host import DhcpHost, DhcpHostAdmin                          # noqa: F401
from .option_type import DhcpOptionType, DhcpOptionTypeAdmin       # noqa: F401
from .range import DhcpRange, DhcpRangeAdmin                       # noqa: F401
from .tag import DhcpTag, DhcpTagAdmin                             # noqa: F401
