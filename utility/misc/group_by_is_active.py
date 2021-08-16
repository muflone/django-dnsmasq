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

from django.db.models import Model


def group_by_is_active(model: Model) -> list[Model]:
    """
    Return the model records by grouping them by is_active
    :param model: model to query
    :return: list of three items [all records, only enabled, only disabled]
    """
    rows = model.objects.all()
    # Add all the records
    results = []
    results.append(rows)
    for value in True, False:
        results.append([row for row in rows if row.is_active == value])
    return results
