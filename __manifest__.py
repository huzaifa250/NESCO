# -*- coding: utf-8 -*-
{
    'name': "NESCO",

    'summary': "Coffee Shop Management System",

    'description': """
It's web application
    """,

    'author': "Huzaifa Elnaeem",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'sale_management', 'stock', 'website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/nesco_coffee_shop_temp.xml',
        'views/create_submit_product_temp.xml',
        'views/update_product_template.xml',
        'views/delete_product_template_view.xml',
        # 'views/dashboard_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'auto_install': False,
}
