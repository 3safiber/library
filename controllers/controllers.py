# -*- coding: utf-8 -*-
# from odoo import http


# class Test2-addon(http.Controller):
#     @http.route('/test2-addon/test2-addon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test2-addon/test2-addon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test2-addon.listing', {
#             'root': '/test2-addon/test2-addon',
#             'objects': http.request.env['test2-addon.test2-addon'].search([]),
#         })

#     @http.route('/test2-addon/test2-addon/objects/<model("test2-addon.test2-addon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test2-addon.object', {
#             'object': obj
#         })

