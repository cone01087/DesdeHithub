# -*- coding: utf-8 -*-
from odoo import http

# class /home/ffgt/enterprise/cigars(http.Controller):
#     @http.route('//home/ffgt/enterprise/cigars//home/ffgt/enterprise/cigars/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/ffgt/enterprise/cigars//home/ffgt/enterprise/cigars/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/ffgt/enterprise/cigars.listing', {
#             'root': '//home/ffgt/enterprise/cigars//home/ffgt/enterprise/cigars',
#             'objects': http.request.env['/home/ffgt/enterprise/cigars./home/ffgt/enterprise/cigars'].search([]),
#         })

#     @http.route('//home/ffgt/enterprise/cigars//home/ffgt/enterprise/cigars/objects/<model("/home/ffgt/enterprise/cigars./home/ffgt/enterprise/cigars"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/ffgt/enterprise/cigars.object', {
#             'object': obj
#         })