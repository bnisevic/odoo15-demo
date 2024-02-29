{
    'name': 'CRM Checklist',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Add checklist feature to CRM',
    'depends': ['base', 'crm'],
    'assets': {
        'web.assets_backend': [
            'crm_checklist/static/src/css/progress_bar.css',
        ],
    },
    'data': [
        'views/crm_checklist_config.xml',
        'views/crm_lead_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
