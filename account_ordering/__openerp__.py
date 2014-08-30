# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo - Account ordering
#       
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Account ordering",
    "version": "1.0",
    "author": "Luis Marti­nez Ontalba",
    "website": "http://www.tecnisagra.com",
    "category": "Enterprise Specific Modules",
    "description": """
This module create a new function field in account moves model showing the relative position of moves ordered by date.
The module includes a new report showing the journal ledger with the new ordering field added. This report is triggered
from the tree view in the account move menu.
Code is based on previous work by Zikzakmedia, Pexego and others. 

            """,
    "depends": [
                'account',
        ],
    "init_xml": [
        ],
    "demo_xml": [
	],
    "update_xml": [
        'account_ordering_view.xml',
	'account_ordering_report.xml',
	],
    "installable": True,
    "active": False,
}
