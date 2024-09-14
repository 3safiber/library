from odoo import models, fields

class MyModel(models.Model):

    _name = 'book.model'    
    _description = 'My book model'
    name = fields.Char(string='Name')
    test = fields.Char(string='Test')
    states = fields.Selection(
        string='state',
        selection=[('draft', 'Draft'), ('done', 'Done'),
        ('test', 'Test'),('test2', 'Test2')
        ]
    )
    
    description = fields.Text()
    postcode= fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms =fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Boolean()