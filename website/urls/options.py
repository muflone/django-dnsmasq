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

from website.views.options.create import OptionsCreateView
from website.views.options.delete import OptionsDeleteView
from website.views.options.detail import OptionsDetailView
from website.views.options.list import OptionsListView


urlpatterns = []

# Options create page
urlpatterns.append(path(route='create',
                        view=OptionsCreateView.as_view(),
                        name='website.options.create'))
# Options delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=OptionsDeleteView.as_view(),
                        name='website.options.delete'))
# Options detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=OptionsDetailView.as_view(),
                        name='website.options.detail'))
# Options list page
urlpatterns.append(path(route='list',
                        view=OptionsListView.as_view(),
                        name='website.options.list'))