from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    deposit_amount = fields.Monetary(string="Deposit Amount")
    project_name = fields.Char(string="Project Name")
    attn = fields.Char(string="Attn")
