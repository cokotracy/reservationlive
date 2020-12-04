"""
    This file is used for create and inherit the core controllers
"""
import json
from odoo.http import request, Controller, route
from odoo import http
import odoo
import logging
from odoo.tools.translate import _
_logger = logging.getLogger(__name__)

class WebsiteExtended(http.Controller):

    @http.route(['/floor/<int:floor_id>'], type='http', auth="public", website=True)
    def display_areas_listing(self,floor_id=False):
        floor_rec = request.env['mk.floor'].sudo().search([('id','=',floor_id)])
        values = {
            'floor' : floor_rec
        }
        return request.render("website_extended.area_listing", values)

    @http.route(['/area/<int:area_id>'], type='http', auth="public", website=True)
    def display_table_listing(self,area_id=False):
        area_rec = request.env['mk.area'].sudo().search([('id','=',area_id)])
        values = {
            'area' : area_rec
        }
        return request.render("website_extended.table_listing", values)