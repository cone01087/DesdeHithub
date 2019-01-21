from odoo import models, fields, api, _
from odoo.exceptions import Warning
from datetime import datetime, timedelta

class Paca(models.Model):
	_inherit = "stock.production.lot"

	state = fields.Selection([('ep','En Proceso'),('fin','Finalizado')],"Estado",default='ep')
	costo = fields.Float("Costo libra $")
	costo_paca = fields.Float("Costo paca", compute='_get_total_paca')
	cantidad = fields.Float("Cantidad")
	mov_materia = fields.Boolean("Mover")
	almacen = fields.Many2one("stock.warehouse", "Almacén") 
	locacion_id = fields.Many2one("stock.location","Ubicación test")
	stock_id = fields.Many2one("stock.location","Ubicación destino")
	partner_id = fields.Many2one("res.partner","Proveedor", domain=[('supplier','=',True)])
	fecha = fields.Date("Fecha de compra/cosecha")
	test_id = fields.Many2one("rezago.test","Test id")

	@api.multi
	def unlink(self):
		if self.mov_materia:
			raise Warning(('No puede borrar este registro'))
		return super(Paca, self).unlink()

	@api.multi
	def set_state(self):
		if not self.id:
			raise Warning(('Primero debe guardar el registro'))

		obj_stock = self.env["stock.picking"]
		lineas = []

		vals= {
			'product_id': self.product_id.id,
			'product_uom_qty': self.cantidad,
			'product_uom': self.product_id.uom_id.id,
			'quantity_done':self.cantidad,
			'name': self.product_id.name
		}

		lineas.append((0, 0, vals))
		values = {
			'partner_id': self.partner_id.id,
			'min_date': datetime.now(),
			'picking_type_id': self.almacen.in_type_id.id,
			'move_type': 'direct',
			'priority': '1',
			'move_lines': lineas,
			'state':'done',
			'location_id': self.almacen.in_type_id.default_location_src_id.id,
			'location_dest_id': self.stock_id.id
		}
		idPick = obj_stock.create(values)
		modiLote = self.env["stock.move.line"].search([('picking_id','=',idPick.id)])
		modiLote.write({
			'lot_id':self.id 
			})

		idPick.button_validate()
		print("/"*500)
		self.write({'state':'fin'})



	@api.onchange("almacen")
	def onchangeprueba(self):
		if self.almacen:
			self.locacion_id = self.almacen.lot_stock_id.id
			print("*"*200)
			print(self.product_id.tipo_materia_id.codigo_materia)
	
	@api.depends("costo", "product_qty")
	def _get_total_paca(self):
		self.costo_paca = self.costo * self.cantidad

	@api.multi
	def set_revertir_materia_prima(self):
		self.env["stock.quant"].search([('lot_id','=',self.id)]).unlink()
		modi = self.env["stock.production.lot"].search([('id','=', self.id)])
		modi.write({
			'mov_materia':False
			})


	@api.multi
	def set_mover_materia_prima(self):
		self.env["stock.quant"].create({
						'product_id':self.product_id.id,
						'location_id':self.stock_id.id,
						'lot_id':self.id,
						'quantity':self.cantidad

					})
		modi = self.env["stock.production.lot"].search([('id','=', self.id)])
		modi.write({
			'mov_materia':True
			})

	@api.model
	def create(self, vals):
		if vals.get("almacen"):
			if vals.get("cantidad") <= 0:
				raise Warning(('La cantidad no puede ser menor  o igual a cero'))

			
		varialble_string = datetime.strptime(vals.get("fecha"),  '%Y-%m-%d')
		vals["name"] = vals.get("name")+"-"+varialble_string.strftime("%Y")
		

		"""if vals.get("costo") <= 0:
			raise Warning(('El costo no puede ser menor  o igual a cero'))"""
		
		return super(Paca,self).create(vals)

class MediasHojas(models.Model):
	_inherit = "stock.quant"
	_rec_name = "lot_id"

	medias_hojas = fields.Integer("1/2 hojas", default=0)

class Ubicacion(models.Model):
	_inherit = "stock.location"

	max_pacas = fields.Integer("# máximo de pacas", default=9)


