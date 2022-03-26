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

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    get_default_password_validators,
    validate_password)
from django.core.validators import MinLengthValidator


class UserPasswordForm(forms.ModelForm):
    new_password = forms.CharField(
        label='Password',
        required=True,
        min_length=1,
        widget=forms.PasswordInput
    )
    new_password_confirm = forms.CharField(
        label='Password confirmation',
        required=True,
        min_length=1,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = []

    def __init__(self, *args, **kwargs):
        """
        Customize the form
        """
        forms.ModelForm.__init__(self, *args, **kwargs)
        # Get the minimum password length requirement
        for validator in get_default_password_validators():
            if isinstance(validator, MinimumLengthValidator):
                min_length = validator.min_length
                break
        else:
            # Set default length
            min_length = 8
        # Set the new minimum length for the password fields
        for field_name in ('new_password', 'new_password_confirm'):
            self.base_fields[field_name].min_length = min_length
            self.declared_fields[field_name].min_length = min_length
            self.fields[field_name].min_length = min_length
            self.fields[field_name].widget.attrs['minlength'] = min_length
            for validator in self.fields[field_name].validators:
                if isinstance(validator, MinLengthValidator):
                    validator.min_length = min_length
                    validator.limit_value = min_length
                    break

    def clean_new_password(self):
        """
        Check the password field
        """
        password = self.cleaned_data['new_password']
        validate_password(password, self.instance)
        return password

    def clean_new_password_confirm(self):
        """
        Check the password confirmation field
        """
        password = self.cleaned_data['new_password_confirm']
        validate_password(password, self.instance)
        return password

    def clean(self):
        """
        Check if both passwords field match
        """
        password1 = self.cleaned_data.get('new_password')
        password2 = self.cleaned_data.get('new_password_confirm')
        if password1 and password1 != password2:
            error = "Passwords don't match"
            self.add_error('new_password', error)
            self.add_error('new_password_confirm', error)
        return self.cleaned_data
