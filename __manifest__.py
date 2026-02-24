# Por qué: módulo stub. El original era de Studio v17 con vistas rotas en v19.
#          Se vacía el data para evitar errores de validación.
# Por qué auto_install=True: Si un build previo lo dejó 'uninstalled',
#          update_module_list lo re-marca como 'to install' ANTES de check_module_states.
#          sale depende de este módulo vía ir_module_module_dependency (Studio v17).
{
    'name': 'Custom Template (deprecated)',
    'version': '1.0.0',
    'category': 'Hidden',
    'summary': 'Stub - Studio templates removed in Odoo 19 upgrade',
    'depends': ['base'],
    'data': [],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
