# -*- coding: utf-8 -*-
# © 2015 Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProcurementGroup(models.Model):

    _inherit = 'procurement.group'

    lot_id = fields.Many2one('stock.production.lot', 'Lot')


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _get_stock_move_values(
            self, product_id, product_qty, product_uom, location_id, name,
            origin, values, group_id):
        result = super()._get_stock_move_values(
            product_id, product_qty, product_uom, location_id,
            name, origin, values, group_id)
        if values.get('lot_id', False):
            result['lot_id'] = values['lot_id']
        return result
