# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    custom_template_id = fields.Many2one('custom.template',string = "Template")
    
