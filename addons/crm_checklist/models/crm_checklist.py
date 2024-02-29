from odoo import models, fields

class CRMChecklist(models.Model):
    _name = 'crm.checklist'
    _description = 'CRM Checklist'

    name = fields.Char(required=True)
    is_checked = fields.Boolean(default=False)
    lead_id = fields.Many2one('crm.lead', ondelete='cascade', string='Lead')
