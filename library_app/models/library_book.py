from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _name = "library.book"
    _description = "Book"
    # String fields
    name = fields.Char("Title")
    isbn = fields.Char("ISBN")
    book_type = fields.Selection(
            [("paper", "Paperback"),
             ("hard", "Hardcover"),
             ("electronic", "Electronic"),
             ("other", "Other")],
            "Type"
    )
    notes = fields.Text("Internal Notes")
    descr = fields.Html("Description"),
    # Numeric fields
    copies = fields.Integer(default=1)
    avg_rating = fields.Float("Average Rating", (3,2))
    price = fields.Monetary("Price", "currency_id")
    # Price helper
    currency_id = fields.Many2one("res.currency")
    # Date and time fields:
    date_published = fields.Date()
    # Other fields:
    active = fields.Boolean("Active?", default=True)
    image = fields.Binary("Cover?")
    # Relational fields
    publisher_id = fields.Many2one("res.partner", string="Publisher")
    author_ids = fields.Many2many("res.partner", string="Authors")
    publisher_country_id = fields.Many2one(
            'res.country', 'Publisher Country',
            compute='_compute_publisher_country',
            inverse='_inverse_publisher_country',
            search='_search_publisher_country',
    )
    _sql_constraints = [
            ("library_book_name_date_uq",
             "UNIQUE (name,date_published)",
             "Title and publication date must be unique."),
            ("library_book_check_date",
             "CHECK (date_published <= current_date)",
             "Publication date must not be in the future."),
            ]

    @api.constrains("isbn")
    def _constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s is an invalid ISBN" % book.isbn)

    @api.depends("publisher_id.country_id")
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [
                ('publisher_id.country_id', operator, value)
                ]

    def _check_isbn(self):
        self.ensure_one()
        ponderations = [1, 3] * 6
        digits = [int(letter) for letter in self.isbn if letter.isdigit()]
        remain = sum(a*b for a,b in zip(digits[:12], ponderations)) % 10
        check = 10 - remain if remain != 0 else 0
        return digits and digits[-1] == check

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
