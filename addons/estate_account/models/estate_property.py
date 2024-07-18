from odoo import Command, models


class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        result = super(EstateProperty, self).action_sold()

        invoice_vals = {
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': 'Selling Price Commission',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06
                }),
                Command.create({
                    'name': 'Administrative Fees',
                    'quantity': 1,
                    'price_unit': 100.00
                })
            ]
        }
        self.env['account.move'].create(invoice_vals)

        return result
