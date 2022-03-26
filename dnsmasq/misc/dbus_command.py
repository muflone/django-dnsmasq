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

import dbus

DBUS_DNSMASQ_BUS_NAME = 'uk.org.thekelleys.dnsmasq'
DBUS_DNSMASQ_OBJECT_PATH = '/uk/org/thekelleys/dnsmasq'


class DbusConfiguration(object):
    def __init__(self,
                 bus_name: str = DBUS_DNSMASQ_BUS_NAME,
                 object_path: str = DBUS_DNSMASQ_OBJECT_PATH):
        self.bus_name = bus_name
        self.object_path = object_path
        self.object = None

    def connect(self) -> bool:
        """
        Connect to the dnsmasq System Bus

        :return: True if the dbus can be acquired
        """
        try:
            self.object = dbus.SystemBus().get_object(
                bus_name=self.bus_name,
                object_path=self.object_path)
        except dbus.exceptions.DBusException:
            self.object = None
        return self.object is not None

    def dhcp_delete_lease(self, address: str) -> bool:
        """
        Remove an address from the leases

        :param address: IP address to remove
        :return: True if the lease was successfully removed
        """
        return self.object.DeleteDhcpLease(address)
