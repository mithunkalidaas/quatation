# -*- coding: utf-8 -*-
# from odoo import http


# class Quatation(http.Controller):
#     @http.route('/quatation/quatation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quatation/quatation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quatation.listing', {
#             'root': '/quatation/quatation',
#             'objects': http.request.env['quatation.quatation'].search([]),
#         })

#     @http.route('/quatation/quatation/objects/<model("quatation.quatation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quatation.object', {
#             'object': obj
#         })
