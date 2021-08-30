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

import pathlib

from django.contrib import messages
from django.views.generic.edit import FormView

from dnsmasq.constants import SETTING_CONFIGURATION_PATH
from dnsmasq.misc.configuration_generator import (ConfigurationGenerator,
                                                  SECTION_HEADERS)

from utility.misc.get_setting_value import get_setting_value

from website.forms.configuration.export import ConfigurationExportForm

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ConfigurationExportView(RequireLoginMixin,
                              GenericMixin,
                              FormView):
    form_class = ConfigurationExportForm
    template_name = 'website/configuration/export.html'
    page_title = 'Export configuration'

    def form_valid(self, form):
        """
        Save data because the form is valid

        :param form: form object
        :return: HttpResponse object
        """
        if setting_value := get_setting_value(name=SETTING_CONFIGURATION_PATH):
            # Export configuration
            generator = ConfigurationGenerator(
                include_descriptions=form.cleaned_data['include_descriptions'],
                show_disabled=form.cleaned_data['show_disabled'])
            results = {key: method()
                       for key, method
                       in generator.configuration_blocks_map.items()}
            # Export configuration to file
            settings_path = pathlib.Path(setting_value)
            if not form.cleaned_data['multiple_files']:
                # Single file configuration
                conf_filename = settings_path / 'dnsmasq.conf'
                # Write file
                with open(conf_filename, 'w') as file:
                    # Add each block
                    for block in generator.configuration_blocks_map.keys():
                        file.write(generator.format_results(results[block]))
            else:
                # Multiple files configuration
                for block in generator.configuration_blocks_map.keys():
                    if block != SECTION_HEADERS:
                        conf_filename = settings_path / f'dnsmasq_{block}.conf'
                        # Write file
                        with open(conf_filename, 'w') as file:
                            file.write(generator.format_results(
                                results[SECTION_HEADERS]))
                            file.write(generator.format_results(
                                results[block]))
            # Add status message
            messages.add_message(request=self.request,
                                 level=messages.SUCCESS,
                                 message='Export successful')
        return self.render_to_response(
            self.get_context_data())
