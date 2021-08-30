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

from django.contrib import messages
from django.views.generic.edit import FormView

from dnsmasq.constants import SETTING_CONFIGURATION_PATH
from dnsmasq.misc.configuration_generator import ConfigurationGenerator

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
        setting_value = get_setting_value(name=SETTING_CONFIGURATION_PATH)
        if setting_value:
            # Export configuration
            configuration_generator = ConfigurationGenerator(
                include_descriptions=form.cleaned_data['include_descriptions'],
                show_disabled=form.cleaned_data['show_disabled'])
            results = []
            results.extend(configuration_generator.process_headers())
            results.extend(configuration_generator.process_options())
            results.extend(configuration_generator.process_interfaces())
            results.extend(configuration_generator.process_listen_addresses())
            results.extend(configuration_generator.process_domains())
            results.extend(configuration_generator.process_dhcp_ranges())
            results.extend(configuration_generator.process_dhcp_options())
            results.extend(configuration_generator.process_dhcp_hosts())
            with open(setting_value, 'w') as file:
                file.write(configuration_generator.format_results(results))
            # Add status message
            messages.add_message(request=self.request,
                                 level=messages.SUCCESS,
                                 message='Export successful')
        return self.render_to_response(
            self.get_context_data())
