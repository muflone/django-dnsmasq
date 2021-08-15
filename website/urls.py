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

from website.views.dashboard import DashboardView

from website.views.auth.login import LoginView
from website.views.auth.logout import LogoutView

from website.views.actions.create import ActionsCreateView
from website.views.actions.delete import ActionsDeleteView
from website.views.actions.detail import ActionsDetailView
from website.views.actions.list import ActionsListView

from website.views.dhcp_option_types.create import DhcpOptionTypesCreateView
from website.views.dhcp_option_types.delete import DhcpOptionTypesDeleteView
from website.views.dhcp_option_types.detail import DhcpOptionTypesDetailView
from website.views.dhcp_option_types.list import DhcpOptionTypesListView

from website.views.dhcp_ranges.create import DhcpRangesCreateView
from website.views.dhcp_ranges.delete import DhcpRangesDeleteView
from website.views.dhcp_ranges.detail import DhcpRangesDetailView
from website.views.dhcp_ranges.list import DhcpRangesListView

from website.views.domains.create import DomainsCreateView
from website.views.domains.delete import DomainsDeleteView
from website.views.domains.detail import DomainsDetailView
from website.views.domains.list import DomainsListView

from website.views.interfaces.create import InterfacesCreateView
from website.views.interfaces.delete import InterfacesDeleteView
from website.views.interfaces.detail import InterfacesDetailView
from website.views.interfaces.list import InterfacesListView

from website.views.listen_addresses.create import ListenAddressesCreateView
from website.views.listen_addresses.delete import ListenAddressesDeleteView
from website.views.listen_addresses.detail import ListenAddressesDetailView
from website.views.listen_addresses.list import ListenAddressesListView

from website.views.options.create import OptionsCreateView
from website.views.options.delete import OptionsDeleteView
from website.views.options.detail import OptionsDetailView
from website.views.options.list import OptionsListView

from website.views.users.create import UsersCreateView
from website.views.users.delete import UsersDeleteView
from website.views.users.detail import UsersDetailView
from website.views.users.list import UsersListView
from website.views.users.password import UsersPasswordView


urlpatterns = []
# Login page
urlpatterns.append(path(route='login',
                        view=LoginView.as_view(),
                        name='website.auth.login'))
# Logout page
urlpatterns.append(path(route='logout',
                        view=LogoutView.as_view(),
                        name='website.auth.logout'))
# Home page
urlpatterns.append(path(route='',
                        view=DashboardView.as_view(),
                        name='website.home'))
# Users list page
urlpatterns.append(path(route='users/list',
                        view=UsersListView.as_view(),
                        name='website.users.list'))
# Users detail page
urlpatterns.append(path(route='users/<int:pk>',
                        view=UsersDetailView.as_view(),
                        name='website.users.detail'))
# Users delete page
urlpatterns.append(path(route='users/delete/<int:pk>',
                        view=UsersDeleteView.as_view(),
                        name='website.users.delete'))
# Users create page
urlpatterns.append(path(route='users/create',
                        view=UsersCreateView.as_view(),
                        name='website.users.create'))
# Users password set
urlpatterns.append(path(route='users/password/<int:pk>',
                        view=UsersPasswordView.as_view(),
                        name='website.users.password'))

# Actions list page
urlpatterns.append(path(route='actions/list',
                        view=ActionsListView.as_view(),
                        name='website.actions.list'))
# Actions detail page
urlpatterns.append(path(route='actions/detail/<int:pk>',
                        view=ActionsDetailView.as_view(),
                        name='website.actions.detail'))
# Actions delete page
urlpatterns.append(path(route='actions/delete/<int:pk>',
                        view=ActionsDeleteView.as_view(),
                        name='website.actions.delete'))
# Actions create page
urlpatterns.append(path(route='actions/create',
                        view=ActionsCreateView.as_view(),
                        name='website.actions.create'))

# Domains list page
urlpatterns.append(path(route='domains/list',
                        view=DomainsListView.as_view(),
                        name='website.domains.list'))
# Domains detail page
urlpatterns.append(path(route='domains/detail/<int:pk>',
                        view=DomainsDetailView.as_view(),
                        name='website.domains.detail'))
# Domains delete page
urlpatterns.append(path(route='domains/delete/<int:pk>',
                        view=DomainsDeleteView.as_view(),
                        name='website.domains.delete'))
# Domains create page
urlpatterns.append(path(route='domains/create',
                        view=DomainsCreateView.as_view(),
                        name='website.domains.create'))

# DHCP option types list page
urlpatterns.append(path(route='dhcp_option_types/list',
                        view=DhcpOptionTypesListView.as_view(),
                        name='website.dhcp_option_types.list'))
# DHCP option types detail page
urlpatterns.append(path(route='dhcp_option_types/detail/<int:pk>',
                        view=DhcpOptionTypesDetailView.as_view(),
                        name='website.dhcp_option_types.detail'))
# DHCP option types delete page
urlpatterns.append(path(route='dhcp_option_types/delete/<int:pk>',
                        view=DhcpOptionTypesDeleteView.as_view(),
                        name='website.dhcp_option_types.delete'))
# DHCP option types create page
urlpatterns.append(path(route='dhcp_option_types/create',
                        view=DhcpOptionTypesCreateView.as_view(),
                        name='website.dhcp_option_types.create'))

# DHCP ranges list page
urlpatterns.append(path(route='dhcp_ranges/list',
                        view=DhcpRangesListView.as_view(),
                        name='website.dhcp_ranges.list'))
# DHCP ranges detail page
urlpatterns.append(path(route='dhcp_ranges/detail/<int:pk>',
                        view=DhcpRangesDetailView.as_view(),
                        name='website.dhcp_ranges.detail'))
# DHCP ranges delete page
urlpatterns.append(path(route='dhcp_ranges/delete/<int:pk>',
                        view=DhcpRangesDeleteView.as_view(),
                        name='website.dhcp_ranges.delete'))
# DHCP ranges create page
urlpatterns.append(path(route='dhcp_ranges/create',
                        view=DhcpRangesCreateView.as_view(),
                        name='website.dhcp_ranges.create'))

# Listening addresses list page
urlpatterns.append(path(route='listen_addresses/list',
                        view=ListenAddressesListView.as_view(),
                        name='website.listen_addresses.list'))
# Listening addresses detail page
urlpatterns.append(path(route='listen_addresses/detail/<int:pk>',
                        view=ListenAddressesDetailView.as_view(),
                        name='website.listen_addresses.detail'))
# Listening addresses delete page
urlpatterns.append(path(route='listen_addresses/delete/<int:pk>',
                        view=ListenAddressesDeleteView.as_view(),
                        name='website.listen_addresses.delete'))
# Listening addresses create page
urlpatterns.append(path(route='listen_addresses/create',
                        view=ListenAddressesCreateView.as_view(),
                        name='website.listen_addresses.create'))

# Interfaces list page
urlpatterns.append(path(route='interfaces/list',
                        view=InterfacesListView.as_view(),
                        name='website.interfaces.list'))
# Interfaces detail page
urlpatterns.append(path(route='interfaces/detail/<int:pk>',
                        view=InterfacesDetailView.as_view(),
                        name='website.interfaces.detail'))
# Interfaces delete page
urlpatterns.append(path(route='interfaces/delete/<int:pk>',
                        view=InterfacesDeleteView.as_view(),
                        name='website.interfaces.delete'))
# Interfaces create page
urlpatterns.append(path(route='interfaces/create',
                        view=InterfacesCreateView.as_view(),
                        name='website.interfaces.create'))

# Options list page
urlpatterns.append(path(route='options/list',
                        view=OptionsListView.as_view(),
                        name='website.options.list'))
# Options detail page
urlpatterns.append(path(route='options/detail/<int:pk>',
                        view=OptionsDetailView.as_view(),
                        name='website.options.detail'))
# Options delete page
urlpatterns.append(path(route='options/delete/<int:pk>',
                        view=OptionsDeleteView.as_view(),
                        name='website.options.delete'))
# Options create page
urlpatterns.append(path(route='options/create',
                        view=OptionsCreateView.as_view(),
                        name='website.options.create'))
