# -*- coding: utf-8 -*-
{
    'name': "Componentes materia prima Inventario",

    'author': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','stock', 'diadema_payroll', 'mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/doff_product.xml',
        'views/doff_origen.xml',
        'views/doff_partner.xml',
        'views/doff_objetos.xml',
        'views/doff_objetos_desnudo.xml',
        'views/stock.xml',
        'views/requisicion.xml',
        'views/users.xml',
        'reports/requisicion_print.xml',
        'reports/requisicion_print_view.xml',
        'views/requisicion_sequence.xml',
        
    ],

    'update_xml': [
       "security/groups.xml",
       "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}