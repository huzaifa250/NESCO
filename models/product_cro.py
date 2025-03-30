from odoo import models, fields
from datetime import timedelta


# class ProductTemplate(models.Model):
#     _inherit = 'product.template'
#
#     def _cron_delete_archived(self):
#         """Delete products archived over 1 hour ago"""
#         expired_products = self.search([
#             ('active', '=', False),
#             ('write_date', '<', fields.Datetime.now() - timedelta(hours=1))
#         ])
#         expired_products.unlink()
