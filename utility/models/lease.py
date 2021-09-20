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

import dataclasses
import datetime
import ipaddress


@dataclasses.dataclass
class Lease(object):
    expiration: int
    mac_address: str
    address: str
    hostname: str
    client_identifier: str

    @staticmethod
    def load_from_string(text: str):
        """
        Load a new Lease object from a string
        :param text: line from a dnsmasq.leases file
        :return: Lease object
        """
        items = text.strip().split(' ')
        return Lease(expiration=int(items[0]),
                     mac_address=items[1].upper(),
                     address=items[2],
                     hostname=items[3],
                     client_identifier=items[4])

    @property
    def expiration_date(self) -> datetime.datetime:
        """
        Get the expiration date
        :return: datetime for the lease expiration
        """
        return datetime.datetime.fromtimestamp(self.expiration)

    @property
    def expire_difference(self):
        """
        Get the expiration difference
        :return: date difference if lease is not expired, else None
        """
        now = datetime.datetime.utcnow().replace(microsecond=0)
        expiration_date = self.expiration_date.replace(microsecond=0)
        return (expiration_date - now
                if now < expiration_date
                else None)

    @property
    def description(self) -> str:
        """
        Filter out the '*' for the hostname
        :return: lease description
        """
        return self.hostname if self.hostname != '*' else ''

    @property
    def address_numeric(self) -> int:
        """
        Get the numeric IP address from the address
        :return: numeric IP address
        """
        return int(ipaddress.ip_address(self.address))
