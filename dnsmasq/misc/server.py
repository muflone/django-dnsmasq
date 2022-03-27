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

import subprocess


class Server(object):
    def __init__(self, name: str, sudo: bool):
        self.name = name
        self.sudo = sudo

    def _systemctl_command(self,
                           command: str,
                           timeout: float) -> subprocess.Popen:
        """
        Execute a command with systemctl

        :param command: systemctl command to execute
        :param timeout: time to await in seconds
        :return: subprocess.Popen instance
        """
        arguments = ['systemctl', command, self.name]
        if self.sudo:
            arguments.insert(0, 'sudo')
        process = subprocess.Popen(args=arguments,
                                   shell=False,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        if timeout:
            process.wait(timeout=timeout)
        return process

    def start(self) -> None:
        """
        Start the service
        """
        self._systemctl_command(command='start', timeout=5)

    def stop(self) -> None:
        """
        Stop the service
        """
        self._systemctl_command(command='stop', timeout=5)

    def is_active(self) -> bool:
        """
        Check if the service is active

        :return: True if the service is active
        """
        process = self._systemctl_command(command='is-active', timeout=0)
        stdout, _ = process.communicate()
        return stdout.decode('utf-8').strip().lower() == 'active'

    def restart(self) -> None:
        """
        Restart the service
        """
        self._systemctl_command(command='restart', timeout=5)
