from odoo import models, fields


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    checklist_ids = fields.One2many('crm.checklist', 'lead_id', string='Checklist')
    checklist_progress = fields.Float(compute='_compute_checklist_progress')

    def _compute_checklist_progress(self):
        for lead in self:
            total = len(lead.checklist_ids)
            checked = len(lead.checklist_ids.filtered(lambda c: c.is_checked))
            lead.checklist_progress = round(100.0 * checked / total, 2) if total else 0
