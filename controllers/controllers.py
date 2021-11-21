# -*- coding: utf-8 -*-
# from odoo import http


# class HmsMrExtension(http.Controller):
#     @http.route('/hms_mr_extension/hms_mr_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hms_mr_extension/hms_mr_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hms_mr_extension.listing', {
#             'root': '/hms_mr_extension/hms_mr_extension',
#             'objects': http.request.env['hms_mr_extension.hms_mr_extension'].search([]),
#         })

#     @http.route('/hms_mr_extension/hms_mr_extension/objects/<model("hms_mr_extension.hms_mr_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hms_mr_extension.object', {
#             'object': obj
#         })
