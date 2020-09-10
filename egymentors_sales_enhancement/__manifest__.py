# -*- coding: utf-8 -*-
{
    'name': "EgyMentors Sales Enhancement",
    'author': 'EgyMentors, Dalia Atef',
    'category': 'Sale',
    'summary': """Sales Enhancement""",
    'website': 'http://www.egymentors.com',
    'license': 'AGPL-3',
    'description': """
""",
    'version': '10.0',
    'depends': ['sale_management', 'stock', 'sales_custome', 'sale_discount_total'],
    'data': [
        'reports/reports.xml',
        'reports/sale_order_report.xml',
        
        'views/specs_conditions.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
