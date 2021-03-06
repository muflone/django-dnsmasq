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

from django.contrib import admin
from django.db import models


class BaseModel(models.Model):
    def __init__(self, *args, **kwargs):
        """Base model for each other model in the application"""
        super().__init__(*args, **kwargs)

    class Meta:
        abstract = True


class BaseModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        """Base Admin model for each other model in the application"""
        super().__init__(model, admin_site)
        # If ModelAdmin ordering is missing apply the ordering of the model
        if not self.ordering:
            self.ordering = model._meta.ordering
