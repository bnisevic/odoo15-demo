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

    def unlink(self):
        related_checklists = self.env['crm.checklist'].search([('config_id', 'in', self.ids)])
        related_checklists.unlink()
        return super().unlink()
