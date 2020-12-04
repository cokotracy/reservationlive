from odoo import models, fields


class TableShape(models.Model):
    _name = 'mk.table.shape'
    _description = 'Shape of a Table'

    name = fields.Char(string='Shape', required=True)