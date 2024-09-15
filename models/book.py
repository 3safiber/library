from odoo import models, fields
from odoo.exceptions import ValidationError

class MyModel(models.Model):

    _name = 'book.model'    
    _description = 'My book model'
    name = fields.Char(string='Name')
    test = fields.Char(string='Test')
    state = fields.Selection(
        string='state',
        selection=[('draft', 'Draft'), ('bending', 'Bending'),
        ('sold', 'Sold')
        ],
        default='draft'
    )
    
    description = fields.Text()
    postcode= fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    
    
    diff = fields.Float(compute='_compute_diff')
    
    increment = fields.Integer()
    
    bedrooms =fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Boolean()
    
    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
      for record in self:
        record.diff = record.expected_price - record.selling_price
            
    @api.onchange('description')
    def _onchange_description(self):
      self.increment +=1
                            
    @api.constrains('bedrooms')
    def _check_bedrooms_valid_number(self):
      for record in self:
        if record.bedrooms < 0 or record.bedrooms >= 30:
          raise ValidationError('please enter a valid number between 0 and 30')    
    
    def action_draft(self):
      for rec in self:
        rec.state = 'draft'
        # rec.write({
        #   'state':'draft'
        # })
        
    def action_bending(self):
      for rec in self:
        rec.state = 'bending'
        
    def action_sold(self):
      for rec in self:
        rec.state = 'sold'