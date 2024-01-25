from odoo import models, fields
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover?")
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")
    
    def _check_isbn(self):
        self.ensure_one()
        ponderations = [1, 3] * 6
        digits = [int(letter) for letter in self.isbn if letter.isdigit()]
        remain = sum(a*b for a,b in zip(digits[:12], ponderations)) % 10
        check = 10 - remain if remain != 0 else 0
        return digits[-1] == check

    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError(
                        "Please provide an ISBN number for %s" % book.name
                )
            check = book._check_isbn()
            if not check:
                raise ValidationError("ISBN %s is not valid." % book.isbn)
        return True
