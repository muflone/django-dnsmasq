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

from website.views.settings.create import ObjectCreateView
from website.views.settings.delete import ObjectDeleteView
from website.views.settings.detail import ObjectDetailView
from website.views.settings.list import ObjectListView


urlpatterns = []

# Settings create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.settings.create'))
# Settings delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.settings.delete'))
# Settings detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.settings.detail'))
# Settings list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.settings.list'))
