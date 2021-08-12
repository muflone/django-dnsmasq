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
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from website.views.require_login import RequireLoginMixin


class UsersDeleteView(RequireLoginMixin,
                      DeleteView):
    model = User
    success_url = reverse_lazy('website.users.list')

    def get(self, request, *args, **kwargs):
        """
        The DeleteView will remove the object when the request was passed
        with the POST method, else it will show a confirmation dialog
        """
        return self.post(request, *args, **kwargs)
