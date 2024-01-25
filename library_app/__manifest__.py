# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Manage library catalog and book lending
    """,

    'description': """
        Simple demo app for a library in Reis' book
    """,

    'author': "Daniel Reis",
    'website': 
        "https://github.com/PackPublishing"
        "/Odoo-15-Development-Essentials",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    "application": True,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/library_menu.xml",
        "views/book_view.xml",
        "views/book_list_template.xml",
    ]
}
