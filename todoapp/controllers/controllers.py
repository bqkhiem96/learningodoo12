# -*- coding: utf-8 -*-
from odoo import http

# class Todoapp(http.Controller):
#     @http.route('/todoapp/todoapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todoapp/todoapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todoapp.listing', {
#             'root': '/todoapp/todoapp',
#             'objects': http.request.env['todoapp.todoapp'].search([]),
#         })

#     @http.route('/todoapp/todoapp/objects/<model("todoapp.todoapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todoapp.object', {
#             'object': obj
#         })