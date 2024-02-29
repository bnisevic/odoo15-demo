from odoo import _, models, fields

class CRMChecklist(models.Model):
    _name = 'crm.checklist'
    _description = _('CRM Lead Checklist')

    is_checked = fields.Boolean(default=False)
    lead_id = fields.Many2one(
        'crm.lead',
        ondelete='cascade',
        string=_('Lead')
    )
    config_id = fields.Many2one(
        'crm.checklist.config',
        required=True,
        ondelete='restrict',
        string=_('Item')
    )
