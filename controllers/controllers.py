# -*- coding: utf-8 -*-
# from odoo import http


# class Trillium(http.Controller):
#     @http.route('/trillium/trillium', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trillium/trillium/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trillium.listing', {
#             'root': '/trillium/trillium',
#             'objects': http.request.env['trillium.trillium'].search([]),
#         })

#     @http.route('/trillium/trillium/objects/<model("trillium.trillium"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trillium.object', {
#             'object': obj
#         })
