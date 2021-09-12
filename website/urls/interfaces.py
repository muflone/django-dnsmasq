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

from website.views.interfaces.create import ObjectCreateView
from website.views.interfaces.delete import ObjectDeleteView
from website.views.interfaces.detail import ObjectDetailView
from website.views.interfaces.list import ObjectListView


urlpatterns = []

# Interfaces create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.interfaces.create'))
# Interfaces delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.interfaces.delete'))
# Interfaces detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.interfaces.detail'))
# Interfaces list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.interfaces.list'))
