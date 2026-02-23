# Por qué: El módulo original (Studio v17) tiene vistas con campos de v17
#          y la validación falla por vistas hermanas con ocapi_bindings.
#          Desactivamos TODO antes del upgrade.
import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    _logger.info("custom_template ROOT 1.0.0: cleanup INICIO (from %s)", version)

    # --- 1. Desactivar TODAS las vistas de custom_template ---
    cr.execute("""
        UPDATE ir_ui_view SET active = false
        WHERE id IN (
            SELECT res_id FROM ir_model_data
            WHERE module = 'custom_template'
              AND model = 'ir.ui.view'
        )
    """)
    if cr.rowcount:
        _logger.info("custom_template: %d vistas DESACTIVADAS", cr.rowcount)

    # --- 2. Desactivar vistas con ocapi_bindings ---
    cr.execute("""
        UPDATE ir_ui_view SET active = false
        WHERE arch_db::text LIKE '%%ocapi_bindings%%'
          AND active = true
    """)
    if cr.rowcount:
        _logger.info("custom_template: %d vistas ocapi DESACTIVADAS", cr.rowcount)

    # --- 3. Desactivar vistas de módulos OCAPI/meli ---
    cr.execute("""
        UPDATE ir_ui_view SET active = false
        WHERE id IN (
            SELECT res_id FROM ir_model_data
            WHERE module IN ('meli_oerp', 'meli_oerp_accounting',
                            'meli_oerp_stock', 'meli_oerp_multiple',
                            'odoo_connector_api')
              AND model = 'ir.ui.view'
        )
        AND active = true
    """)
    if cr.rowcount:
        _logger.info("custom_template: %d vistas OCAPI/meli DESACTIVADAS", cr.rowcount)

    # --- 4. Limpiar ir_model_data ---
    cr.execute("""
        DELETE FROM ir_model_data
        WHERE module = 'custom_template'
          AND model != 'ir.module.module'
    """)
    if cr.rowcount:
        _logger.info("custom_template: %d ir_model_data ELIMINADOS", cr.rowcount)

    _logger.info("custom_template ROOT 1.0.0: cleanup FIN")
