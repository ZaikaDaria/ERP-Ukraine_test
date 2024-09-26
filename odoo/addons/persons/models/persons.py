from odoo.odoo import models, fields, api
from datetime import date


class Persons(models.Model):
    _name = 'persons'
    _description = 'Person Model'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    full_name = fields.Char(string='Full Name', compute='_compute_full_name')
    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age')
    sex = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('non-binary', 'Non-binary')],
        string='Sex'
    )
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                today = date.today()
                record.age = today.year - record.birthday.year - (
                        (today.month, today.day) < (record.birthday.month, record.birthday.day)
                )
            else:
                record.age = 0
