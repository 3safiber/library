from odoo import models, fields


class LibraryBook(models.Model):

    _name = "library.book"
    _description = "Book"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # add chatter to model
    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author", required=True)
    publisher = fields.Char(string="Publisher")
    description = fields.Text(string="Description")
    publication_date = fields.Date(string="Publication Date")
    selling_price = fields.Float()
    category_id = fields.Many2one('library.category', string="Category")

    state = fields.Selection(
        string="State",
        selection=[
            ("available", "Available"),
            ("reserved", "Reserved"),
            ("borrowed", "Borrowed"),
            ("damaged", "Damaged"),
        ],
        default="available",
    )

    _sql_constraints = [('unique_name', 'unique("name")', 'This name is exist!')]

    def action_available(self):
        for rec in self:
            rec.state = "available"

    def action_reserved(self):
        for rec in self:
            rec.state = "reserved"

    def action_borrowed(self):
        for rec in self:
            rec.state = "borrowed"

    def action_damaged(self):
        for rec in self:
            rec.state = "damaged"
