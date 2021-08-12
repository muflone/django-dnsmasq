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
from django.views.generic import UpdateView

from website.forms.user_password import UserPasswordForm

from website.views.generic import GenericMixin
from website.views.require_superuser import RequireSuperUserMixin


class UsersPasswordView(RequireSuperUserMixin,
                        GenericMixin,
                        UpdateView):
    model = User
    form_class = UserPasswordForm
    template_name = 'website/users/password.html'
    page_title = 'User password set'

    def get_success_url(self):
        """
        Get the returning page after processing the form
        """
        return reverse_lazy('website.users.detail',
                            args=[self.kwargs['pk']])

    def form_valid(self, form):
        """
        Execute the password change
        """
        self.object.set_password(form.cleaned_data['new_password'])
        self.object.save()
        return super().form_valid(form)
