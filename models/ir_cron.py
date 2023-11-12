# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def cron_update_db_expiry_date(self):
        db_expiry = self.env['ir.config_parameter'].sudo().search([('key', '=', 'database.expiration_date')])
        db_expiry.value = '2050-04-02 13:19:19'
