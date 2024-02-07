from odoo import api, exceptions, fields, models

class CheckoutMassMessage(models.TransientModel):
    _name = "library.checkout.massmessage"
    _description = "Send Message to Borrowers"
    checkout_ids = fields.Many2many("library.checkout", string="Checkouts")
    message_subject = fields.Char()
    message_body = fields.Html()