from odoo import models, fields, api


class Table(models.Model):
    _name = 'mk.table'
    _description = 'Table'

    def make_table_available(self):
        self.state = 'available'

    def clean_table(self):
        self.state = 'cleaning'

    @api.onchange('area_id')
    def onchange_area_id(self):
        if self.area_id and self.area_id.floor_id:
            self.floor_id = self.area_id.floor_id.id

    @api.model
    def create(self, vals):
        res = super(Table, self).create(vals)
        if res:
            if res.area_id and res.area_id.floor_id:
                res.floor_id = res.area_id.floor_id.id
        return res

    def make_reservation_from_kanban(self):
        action = self.env["ir.actions.actions"]._for_xml_id("mk_reservation.action_mk_reservation_make_popup")
        action['views'] = [(self.env.ref('mk_reservation.form_mk_reservation_make_popup').id, 'form')]
        context = {}
        if self.floor_id:
            context.update({'default_floor_id': self.floor_id.id})
        if self.area_id:
            context.update({'default_area_id': self.area_id.id})
        context.update({'default_table_id': self.id})
        action['context'] = context
        return action

    def _set_colors(self):
        for table in self:
            if table.state == 'available':
                table.color = 10
            if table.state == 'reserved':
                table.color = 1
            if table.state == 'cleaning':
                table.color = 2

    area_id = fields.Many2one('mk.area', string='Area', copy=False)
    floor_id = fields.Many2one('mk.floor', string='Floor', copy=False, readonly=1)
    name = fields.Char(string='Table Name', required=True)
    shape_id = fields.Many2one('mk.table.shape', string='Shape')
    state = fields.Selection(selection=[('reserved', 'Reserved'),
                                        ('cleaning', 'Cleaning In Progress'),
                                        ('available', 'Open'),], default='available', string="Status")
    color = fields.Integer(string='Color', compute="_set_colors")
    reservation_ids = fields.One2many('mk.make.reservation', 'reservation_table_id', string='Reservations')
    seats = fields.Integer(string='Seats')