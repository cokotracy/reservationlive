from odoo import models, fields, _


class TimeSlot(models.Model):
    _name = 'mk.time.slot'
    _description = 'Time Slot for Reservation'

    def name_get(self):
        res = []
        for slot in self:
            time_from = ('{0:02.0f}:{1:02.0f}'.format(*divmod(float(slot.time_from) * 60, 60)))
            time_to = ('{0:02.0f}:{1:02.0f}'.format(*divmod(float(slot.time_to) * 60, 60)))
            res.append((slot.id, _("From %s To %s") % (time_from, time_to)))
        return res

    name = fields.Char(string='Slot Name', required=True)
    time_from = fields.Float(string='From')
    time_to = fields.Float(string='To')