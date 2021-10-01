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

from django.views.generic.edit import FormView

from dnsmasq.constants import (SETTING_DISPLAY_INCLUDE_DESCRIPTIONS,
                               SETTING_DISPLAY_SHOW_DISABLED_OPTIONS)
from dnsmasq.misc.configuration_generator import ConfigurationGenerator

from utility.misc.get_setting_value import get_setting_value

from website.forms.configuration.display import ConfigurationDisplayForm

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ObjectDisplayView(RequireLoginMixin,
                        GenericMixin,
                        FormView):
    form_class = ConfigurationDisplayForm
    template_name = 'website/tools/configuration/display.html'
    page_title = 'Display configuration'

    def form_valid(self, form):
        """
        Save data because the form is valid

        :param form: form object
        :return: HttpResponse object
        """
        generator = ConfigurationGenerator(
            include_descriptions=form.cleaned_data['include_descriptions'],
            show_disabled=form.cleaned_data['show_disabled'])
        results = []
        for method in generator.configuration_blocks_map.values():
            results.extend(method())
        return self.render_to_response(self.get_context_data(
            results=generator.format_results(results)))

    def get_initial(self):
        """
        Set initial values for form
        :return: dict with initial values
        """
        initial = super().get_initial()
        initial['include_descriptions'] = get_setting_value(
            name=SETTING_DISPLAY_INCLUDE_DESCRIPTIONS,
            default_value='0') == '1'
        initial['show_disabled'] = get_setting_value(
            name=SETTING_DISPLAY_SHOW_DISABLED_OPTIONS,
            default_value='0') == '1'
        return initial
