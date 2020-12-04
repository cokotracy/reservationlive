from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Reservation(models.Model):
    _name = 'mk.make.reservation'
    _description = 'Make Reservation of a Table'

    @api.onchange('floor_id')
    def onchange_floor_id(self):
        domain = {}
        domain['area_id'] = [('name', '=', 'odoo,dev,getodoo,mk')]
        area_ids = []
        if self.floor_id:
            for area_id in self.floor_id.area_ids:
                area_ids.append(area_id.id)
        if area_ids:
            domain['area_id'] = [('id', 'in', area_ids)]
        return {'domain': domain}

    @api.onchange('area_id')
    def onchange_area_id(self):
        domain = {}
        domain['table_id'] = [('name', '=', 'odoo,dev,getodoo,mk')]
        table_ids = []
        if self.area_id:
            for table_id in self.area_id.table_ids:
                if table_id.state != 'reserved':
                    table_ids.append(table_id.id)
        if table_ids:
            domain['table_id'] = [('id', 'in', table_ids)]
        return {'domain': domain}

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            if self.partner_id.mobile:
                self.mobile = self.partner_id.mobile
            if self.partner_id.phone:
                self.phone = self.partner_id.phone
            if self.partner_id.email:
                self.email = self.partner_id.email

    def reserve_table(self):
        if not self.table_id:
            raise ValidationError(_('''Please select Table'''))
        self.state = 'reserved'
        self.table_id.state = 'reserved'
        self.reservation_table_id = self.table_id.id

    name = fields.Char(string='Description', required=True)
    user_id = fields.Many2one('res.users', string='Reserved By', default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Customer')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    floor_id = fields.Many2one('mk.floor', string='Floor', required=True)
    area_id = fields.Many2one('mk.area', string='Area', required=True)
    table_id = fields.Many2one('mk.table', string='Table', required=True)
    reservation_date = fields.Date(string='Reservation Date', required=True)
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('reserved', 'Table Reserved')], default='draft', string="Status")
    time_slot_id = fields.Many2one('mk.time.slot', string='Time Slot')
    remarks = fields.Text(string='Remarks')
    available_seats = fields.Integer(string='Available Seats', related='table_id.seats', readonly=True)
    seats_to_reserve = fields.Integer(string='Seats to Reserve', default=1)
    # used to link reservation with table
    reservation_table_id = fields.Many2one('mk.table', string='Table', copy=False)