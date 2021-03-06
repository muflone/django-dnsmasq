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

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from website.views.generic import GenericMixin
from website.views.require_superuser import RequireSuperUserMixin


class ObjectCreateView(RequireSuperUserMixin,
                       GenericMixin,
                       CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email',
              'is_active', 'is_staff', 'is_superuser']
    success_url = reverse_lazy('website.users.list')
    template_name = 'website/users/detail.html'
    page_title = 'Create new user'
