# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    x_studio_anticipo_financiero = fields.Char(
         string='Forma de pago diferente a cheques',
         copy=True,          # "Copiado" ✓
         tracking=True,      # "Activar el seguimiento de órdenes" ✓ (aparece en el chatter)
         translate=False,    # "Traducible" ✗
         index=False,        # "Indexado" ✗
         help=False,         # "Campo de ayuda" vacío
         # store=True        # Char ya es almacenado por defecto; no hace falta ponerlo
         # required=False    # No obligatorio (default)
         # readonly=False    # No solo lectura (default)
    )
    x_studio_1_cobro = fields.Float(string='1° Cobro')
    x_studio_1_valor = fields.Integer(string='1° Valor')
    x_studio_2_cobro = fields.Float(string='2° Cobro')
    x_studio_2_valor = fields.Integer(string='2° Valor')
    x_studio_3_cobro = fields.Float(string='3° Cobro')
    x_studio_3_valor = fields.Integer(string='3° Valor')
    x_studio_4_cobro = fields.Float(string='4° Cobro')
    x_studio_4_valor = fields.Integer(string='4° Valor')
    x_studio_5_cobro = fields.Float(string='5° Cobro')
    x_studio_5_valor = fields.Integer(string='5° Valor')
    x_studio_6_cobro = fields.Float(string='6° Cobro')
    x_studio_6_valor = fields.Integer(string='6° Valor')
    x_studio_7_cobro = fields.Float(string='7° Cobro')
    x_studio_7_valor = fields.Integer(string='7° Valor')
    x_studio_8_cobro = fields.Float(string='8° Cobro')
    x_studio_8_valor = fields.Integer(string='8° Valor')
    x_studio_9_cobro = fields.Float(string='9° Cobro')
    x_studio_9_valor = fields.Integer(string='9° Valor')
    x_studio_10_cobro = fields.Float(string='10° Cobro')
    x_studio_10_valor = fields.Integer(string='10° Valor')
    x_studio_11_cobro = fields.Float(string='11° Cobro')
    x_studio_11_valor = fields.Integer(string='11° Valor')
    x_studio_12_cobro = fields.Float(string='12° Cobro')
    x_studio_12_valor = fields.Integer(string='12° Valor')
   


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    x_studio_plazo_de_entrega = fields.Char(string='Plazo de entrega')
