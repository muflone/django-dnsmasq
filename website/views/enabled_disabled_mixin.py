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

from django.views.generic.base import ContextMixin


class EnabledDisabledMixin(ContextMixin):
    """Mixin with enabled and disabled rows"""

    def get_context_data(self, **kwargs):
        """
        Get the context data (extra_content is loaded only in GenericMixin)
        """
        context = super().get_context_data(**kwargs)
        # Add objects_enabled using ObjectsEnabled or using filter
        context['object_enabled_list'] = (
            self.model.objects_enabled.all()
            if hasattr(self.model, 'objects_enabled')
            else self.model.objects.filter(is_active=True))
        # Add objects_disabled using ObjectsDisabled or using filter
        context['object_disabled_list'] = (
            self.model.objects_disabled.all()
            if hasattr(self.model, 'objects_disabled')
            else self.model.objects.filter(is_active=False))
        return context
