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

from dnsmasq.misc.configuration_generator import ConfigurationGenerator

from website.forms.configuration import ConfigurationForm

from website.views.generic import GenericMixin
from website.views.require_login import RequireLoginMixin


class ConfigurationView(RequireLoginMixin,
                        GenericMixin,
                        FormView):
    form_class = ConfigurationForm
    template_name = 'website/tools/configuration.html'
    page_title = 'Generate configuration'

    def form_valid(self, form):
        """
        Save data because the form is valid

        :param form: form object
        :return: HttpResponse object
        """
        configuration_generator = ConfigurationGenerator(
            include_descriptions=form.cleaned_data['include_descriptions'])
        results = configuration_generator.process()
        return self.render_to_response(
            self.get_context_data(results=results))
