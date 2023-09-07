
# -*- coding: utf-8 -*-
# © 2015 Akretion (http://www.akretion.com).
# @author Valentin CHEMIERE <valentin.chemiere@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    lot_id = fields.Many2one('stock.production.lot')

    def _update_reserved_quantity(
            self, need, available_quantity, location_id, lot_id=None,
            package_id=None, owner_id=None, strict=True):
        if not lot_id and self.lot_id:
            lot_id = self.lot_id
        return super()._update_reserved_quantity(
            need, available_quantity, location_id, lot_id, package_id,
            owner_id, strict)
