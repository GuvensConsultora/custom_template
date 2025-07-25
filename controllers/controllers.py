# -*- coding: utf-8 -*-
# from odoo import http


# class CustomTemplate(http.Controller):
#     @http.route('/custom_template/custom_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_template/custom_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_template.listing', {
#             'root': '/custom_template/custom_template',
#             'objects': http.request.env['custom_template.custom_template'].search([]),
#         })

#     @http.route('/custom_template/custom_template/objects/<model("custom_template.custom_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_template.object', {
#             'object': obj
#         })

