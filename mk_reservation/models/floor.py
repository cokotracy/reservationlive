from odoo import models, fields


class Floor(models.Model):
    _name = 'mk.floor'
    _description = 'Floor'

    name = fields.Char(string='Floor Name', required=True)
    area_ids = fields.One2many('mk.area', 'floor_id', string='Areas')