from odoo import _, api, models, fields


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    checklist_ids = fields.One2many(
        'crm.checklist',
        'lead_id',
        string=_('Checklist')
    )
    checklist_progress = fields.Float(compute='_compute_checklist_progress')

    def _compute_checklist_progress(self):
        for lead in self:
            total = len(lead.checklist_ids)
            checked = len(lead.checklist_ids.filtered(lambda c: c.is_checked))
            lead.checklist_progress = round(100.0 * checked / total, 2) if total else 0

    @api.model
    def create(self, vals):
        lead = super().create(vals)
        checklist_config_ids = self.env['crm.checklist.config'].search([('user_id', '=', self.env.uid)])
        for config in checklist_config_ids:
            self.env['crm.checklist'].create({
                'lead_id': lead.id,
                'config_id': config.id,
            })
        return lead

    def read(self, fields=None, load='_classic_read'):
        result = super().read(fields, load)
        for record in self:
            checklist_config_ids = self.env['crm.checklist.config'].search([('user_id', '=', self.env.uid)])
            for config in checklist_config_ids:
                checklist_item = self.env['crm.checklist'].search([
                    ('lead_id', '=', record.id),
                    ('config_id', '=', config.id),
                ], limit=1)
                if not checklist_item:
                    self.env['crm.checklist'].create({
                        'lead_id': record.id,
                        'config_id': config.id,
                    })
        return result
