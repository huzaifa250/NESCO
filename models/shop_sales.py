# from odoo import models, fields, api
#
#
# class CoffeeShopSales(models.Model):
#     _name = 'coffee.shop.sales'
#
#     @api.model
#     def calculate_total_sales(self):
#         # Fetch all confirmed sale orders
#         confirmed_orders = self.env['sale.order'].search([('state', '=', 'sale')])
#         # Sum up the total amounts of the sale orders
#         total_sales = sum(confirmed_orders.mapped('amount_total'))
#         return total_sales
#
