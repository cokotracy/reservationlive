from odoo import models, fields


class Area(models.Model):
    _name = 'mk.area'
    _description = 'Area of a Floor'

    name = fields.Char(string='Area Name', required=True)
    floor_id = fields.Many2one('mk.floor', string='Floor')
    table_ids = fields.One2many('mk.table', 'area_id', string='Tables')