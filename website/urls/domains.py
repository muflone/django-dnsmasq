##
#     Project: Django website
# Description: A Django application to create website configuration
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

from django.urls import path

from website.views.domains.create import DomainsCreateView
from website.views.domains.delete import DomainsDeleteView
from website.views.domains.detail import DomainsDetailView
from website.views.domains.list import DomainsListView


urlpatterns = []

# Domains create page
urlpatterns.append(path(route='create',
                        view=DomainsCreateView.as_view(),
                        name='website.domains.create'))
# Domains delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=DomainsDeleteView.as_view(),
                        name='website.domains.delete'))
# Domains detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=DomainsDetailView.as_view(),
                        name='website.domains.detail'))
# Domains list page
urlpatterns.append(path(route='list',
                        view=DomainsListView.as_view(),
                        name='website.domains.list'))
