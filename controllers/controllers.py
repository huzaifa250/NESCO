# -*- coding: utf-8 -*-


from odoo import http, fields
from odoo.http import request
import logging
from odoo.exceptions import ValidationError
from odoo.exceptions import AccessError, UserError

_logger = logging.getLogger(__name__)


class CoffeeShop(http.Controller):
    @http.route('/products', auth='public', website=True)
    def list_products(self, **kwargs):
        # get all the products from the product table
        products = request.env['product.template'].sudo().search([])

        # Calculate total sales
        total_sales = sum(request.env['sale.order'].search([('state', '=', 'sale')]).mapped('amount_total'))
        # Check if no products are found
        if not products:
            # Render a template for no products or pass a message to the existing template
            return request.render('nesco.coffee_shop_temp', {
                'my_products': [],
                'error_message': 'No products available at the moment.'
            })

        # if products are found pass data to the template
        return request.render('nesco.coffee_shop_temp', {
            'my_products': products,
            'list_price': products.mapped('list_price'),
            # 'list_price': products.mapped('list_price'),
            'total_sales': total_sales,
            'error_message': False  # No error, so no message
        })

    # Route for new product creation form page
    @http.route('/new/product', type='http', auth='public', website=True, csrf=True)
    def create_product_form(self, **kwargs):
        return request.render("nesco.create_submit_product_temp")

    # Route to handle form submission for creating a new product
    @http.route('/submit/product', auth='public', website=True, csrf=True)
    def submit_product(self, **kwargs):
        # allow users to create product
        name = kwargs.get('name')  # product name
        # Log the received data
        _logger.info(
            f"Received data: name={name}")
        product = request.env['product.template'].sudo().create(
            {'name': name,
             })
        # print("Name is *************** ", name)
        _logger.info(f"product created: {product}")
        # _logger.error(f"Error creating product:")
        # Redirect or render a success page after creation
        return request.redirect('/products')

    @http.route('/update/product', type='http', auth='user', website=True, csrf=True)
    def update_product(self, **kwargs):
        try:
            product_id = kwargs.get('product_id')
            new_name = kwargs.get('name')

            if not product_id or not new_name:
                raise UserError("Product ID and new name are required.")

            product_id = int(product_id)
            product = request.env['product.template'].sudo().browse(product_id)
            if not product.exists():
                raise UserError("Product not found!")

            product.write({'name': new_name})
            return request.redirect('/products')
        except (UserError, ValueError) as e:
            _logger.error(f"Update error: {e}")
            return request.render("nesco.update_product_temp", {
                'error_message': str(e)
            })
        except Exception as e:
            _logger.error(f"Unexpected error: {e}")
            return request.redirect('/products')

    @http.route('/delete/product', type='http', auth='user', website=True, csrf=True)
    def delete_product(self, **kwargs):
        try:
            # Get product_id from form submission
            product_id = kwargs.get('product_id')
            if not product_id:
                raise UserError("Product ID is required !")

            product_id = int(product_id)
            product = request.env['product.template'].sudo().browse(product_id)

            if not product.exists():
                raise UserError("Product not found.")

            # For safety, soft delete (archive)
            # product.write({'active': False})

            # permanently delete (use cautiously)
            product.unlink()

            return request.redirect('/products')

        except (UserError, ValueError) as e:
            _logger.error(f"Deletion error: {e}")
            return request.render("nesco.delete_product_temp", {
                'error_message': str(e)
            })
        except Exception as e:
            _logger.error(f"Unexpected error: {e}")
            return request.redirect('/products')
