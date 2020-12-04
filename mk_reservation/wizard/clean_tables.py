from odoo import models, fields, _
from odoo.exceptions import ValidationError


class CleanTables(models.TransientModel):
    _name = "clean.tables"

    def clean_selected_tables(self):
        if not self.table_ids:
            raise ValidationError(_('''Please select Tables'''))
        for table_id in self.table_ids:
            table_id.state = 'cleaning'

    table_ids = fields.Many2many('mk.table', string='Tables', domain=[('state', '!=', 'cleaning')])