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

from django.urls import path

from website.views.domains.create import ObjectCreateView
from website.views.domains.delete import ObjectDeleteView
from website.views.domains.detail import ObjectDetailView
from website.views.domains.disable import ObjectDisableView
from website.views.domains.enable import ObjectEnableView
from website.views.domains.list import ObjectListView


urlpatterns = []

# Domains create page
urlpatterns.append(path(route='create',
                        view=ObjectCreateView.as_view(),
                        name='website.domains.create'))
# Domains delete page
urlpatterns.append(path(route='delete/<int:pk>',
                        view=ObjectDeleteView.as_view(),
                        name='website.domains.delete'))
# Domains detail page
urlpatterns.append(path(route='detail/<int:pk>',
                        view=ObjectDetailView.as_view(),
                        name='website.domains.detail'))
# Domains disable page
urlpatterns.append(path(route='disable/<int:pk>',
                        view=ObjectDisableView.as_view(),
                        name='website.domains.disable'))
# Domains enable page
urlpatterns.append(path(route='enable/<int:pk>',
                        view=ObjectEnableView.as_view(),
                        name='website.domains.enable'))
# Domains list page
urlpatterns.append(path(route='list',
                        view=ObjectListView.as_view(),
                        name='website.domains.list'))
