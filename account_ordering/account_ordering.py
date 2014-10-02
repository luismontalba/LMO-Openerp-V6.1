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

from osv import fields, osv
from tools.translate import _

class account_ordering(osv.osv):
    _inherit = "account.move"
    _name = "account.move"
    _order ="date,id asc"
        
    def _get_position(self, cr, uid, ids, field_name, arg, context=None):
        if context is None:
            context = {}
        result = {}
        yearslist = self.pool.get('account.fiscalyear').search(cr, uid, [], offset=0, limit=None, order="id asc", context=None)
        for year in yearslist:
            idlist = self.search(cr, uid, [('fiscalyear_id','=',year)], offset=0, limit=None, order="date, id asc", context=None, count=False)
            i = 0
            for id in idlist:
                result[idlist[i]]=i+1
                i += 1
        return result

    _columns = {
        'fiscalyear_id': fields.related('period_id','fiscalyear_id',type='many2one',relation='account.fiscalyear',string='Fiscal year', readonly=True),
        'order': fields.function(
            _get_position,
            type = "integer",
            obj = "account.move",
            method=True,
            string = "Ord.",
            store=False,
            )   
	}
   	
account_ordering()
