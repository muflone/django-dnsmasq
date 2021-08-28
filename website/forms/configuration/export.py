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

from django import forms

from dnsmasq.constants import SETTING_CONFIGURATION_PATH

from utility.misc.get_setting_value import get_setting_value


class ConfigurationExportForm(forms.Form):
    include_descriptions = forms.BooleanField(label='Include descriptions',
                                              required=False)
    show_disabled = forms.BooleanField(label='Show disabled options',
                                       required=False)
    configuration_path = forms.CharField(label='Configuration path',
                                         required=False,
                                         widget=forms.HiddenInput)

    def get_initial_for_field(self, field, field_name):
        if field_name == 'configuration_path':
            return get_setting_value(name=SETTING_CONFIGURATION_PATH)

    def clean_configuration_path(self):
        configuration_path = get_setting_value(name=SETTING_CONFIGURATION_PATH)
        if not configuration_path:
            self.add_error(field='configuration_path',
                           error='Missing configuration path')
        return configuration_path
