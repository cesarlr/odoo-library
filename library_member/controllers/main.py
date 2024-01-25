# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.library_app.controllers.main import Books

class BooksExtended(Books):

      @http.route()
      def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get("available"):
            all_books = response.qcontext["books"]
            available_books = all_books.filtered("is_available")
            response.qcontext["books"] = available_books
        return response

#     @http.route('/library_app/library_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_app.listing', {
#             'root': '/library_app/library_app',
#             'objects': http.request.env['library_app.library_app'].search([]),
#         })

#     @http.route('/library_app/library_app/objects/<model("library_app.library_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_app.object', {
#             'object': obj
#         })
