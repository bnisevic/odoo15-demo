from odoo import _, models, fields

class CRMChecklistConfig(models.Model):
    _name = 'crm.checklist.config'
    _description = _('CRM Checklist Configuration')

    name = fields.Char(required=True)
    user_id = fields.Many2one(
        'res.users',
        string=_('User'),
        default=lambda self: self.env.uid
    )
