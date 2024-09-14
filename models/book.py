from odoo import models, fields

class MyModel(models.Model):
    _name = 'book.model'
    
    _description = 'My book model'
    
    name = fields.Char(string='Name')
    
    # states = fields.Selection(
    #     string='state',
    #     selection=[('draft', 'Draft'), ('done', 'Done')]
    # )
    
    
