# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NoteOrderLine(models.Model):
    _name = 'note.order.line'
    _inherit = 'sale.order.line'
    
    to_sale = fields.Boolean(string = 'To Sale')
    to_request = fields.Boolean(string = 'To Request', compute = '_compute_to_request_value')
    
    
    invoice_lines = fields.Many2many('account.move.line', 'note_order_line_invoice_rel', 'note_order_line_id', 'invoice_line_id', string='Invoice Lines', copy=False)
    

#     @api.depends('value')
    def _compute_to_request_value(self):
        for record in self:
            pass