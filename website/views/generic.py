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

from django.views.generic import View
from django.views.generic.base import ContextMixin

from dnsmasq.constants import MODE_EASY_SETUP

from project import PRODUCT_NAME, VERSION


class GenericMixin(ContextMixin,
                   View):
    """Generic mixin"""
    extra_context = {
        'app_name': PRODUCT_NAME,
        'app_version': VERSION,
        MODE_EASY_SETUP: MODE_EASY_SETUP
    }

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        context['request_path'] = self.request.path
        context['request_name'] = self.request.resolver_match.url_name
        context['page_title'] = self.page_title
        context['mode'] = self.kwargs.get('mode')
        if hasattr(self, 'column_headers'):
            context['column_headers'] = self.column_headers
        return context
