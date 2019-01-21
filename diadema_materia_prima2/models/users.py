from odoo import models, fields, api

class DoffUsers(models.Model):
    _inherit = "res.users"

    almacenes_ids = fields.Many2many("stock.warehouse", "almacenes_usuarios_rel", "usuario_id", "almacen_id", string="Almacenes permitidos")
    conductor = fields.Boolean("Conductor")
   
class DoffStock(models.Model):
    _inherit = "stock.warehouse"

    usuarios_ids = fields.Many2many("res.users", "almacenes_usuarios_rel", "almacen_id", "usuario_id", string="Usuarios permitidos")