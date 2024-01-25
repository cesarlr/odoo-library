from odoo import models,fields


class Member(models.Model):
    _name = 'library.member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Member'
    card_number = fields.Char()
    partner_id = fields.Many2one(
            'res.partner',
            delegate=True,
            ondelete='cascade',
            required=True)
    
