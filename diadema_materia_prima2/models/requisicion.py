from odoo import models, fields, api
from odoo.exceptions import Warning
from datetime import datetime, timedelta

class Test(models.Model):
	_name = "doff.requisicion"
	_inherit = ['mail.thread']

	def get_default_user_compra(self):
		return self.env.user.id

	@api.one 
	@api.depends('stock_ids.cantidad')
	def get_totales(self):
		contaBul = 0
		contaPeso = 0
		
		for t in self.stock_ids:
			contaBul += 1
			contaPeso += t.cantidad
		
		self.total_bultos = contaBul
		self.total_peso = contaPeso


	proveedor = fields.Many2one("res.partner","Proveedor", domain=[('supplier','=',True)], track_visibility='onchange')
	state = fields.Selection([('borrador','Borrador'),('ingresado','Ingresado'),('anu','Anulado'),('fin','Finalizado')],"Estado",default='borrador', track_visibility='onchange')
	almacen_id = fields.Many2one("stock.warehouse", "Almacén") 
	locacion_id = fields.Many2one("stock.location","Ubicación test")
	fecha = fields.Date("Fecha de registro", track_visibility='onchange')
	encargado_compras = fields.Many2one("res.users","Encargado de compras", track_visibility='onchange')
	encargado_bodega = fields.Many2one("res.users","Encargado de bodega", default=get_default_user_compra, track_visibility='onchange')
	idPick = fields.Many2one("stock.picking","Pick")
	stock_ids = fields.One2many("stock.production.lot", "test_id", "Lotes")
	total_bultos = fields.Integer("Total bultos", compute=get_totales)
	total_peso = fields.Float("Total peso neto", compute=get_totales)
	observaciones = fields.Text("Observaciones")
	name = fields.Char("Numero de Requisición", default=lambda self: self.env['ir.sequence'].get('rq_mprima'))
	
	@api.multi
	def unlink(self):
		if (self.state == "ingresado") or (self.state == "fin"):
			raise Warning(('No puede borrar este registro'))

		return super(Test, self).unlink()

	@api.onchange("almacen_id")
	def onchangeprueba(self):
		if self.almacen_id:
			self.locacion_id = self.almacen_id.lot_stock_id.id
			#obj = 
			#cantidad_pacas


	
	@api.multi
	def anular_picking(self):
		
		borrar = self.env["stock.move.line"].search([('picking_id','=',self.idPick.id)])
		borrar.write({
			'state':'draft'
			})
		self.env["stock.move.line"].search([('picking_id','=',self.idPick.id)]).unlink()

		borrar2 = self.env["stock.move"].search([('picking_id','=',self.idPick.id)])
		borrar2.write({
			'state':'draft'
			})
		self.env["stock.move"].search([('picking_id','=',self.idPick.id)]).unlink()
		
		borrar3 = self.env["stock.picking"].search([('id','=',self.idPick.id)])
		
		borrar3.write({
			'state':'draft'
		})
			
		self.env["stock.picking"].search([('id','=',self.idPick.id)]).unlink()
		
		self.write({'state':'borrador'})


	@api.multi
	def change_state_process(self):
		self.write({'state':'fin'})

	@api.multi
	def change_state_borrador(self):
		self.write({'state':'borrador'})

	@api.multi
	def set_picking(self):
		if not self.id:
			raise Warning(('Primero debe guardar el registro'))
		
		conta = 0
		for veri in self.stock_ids:
			conta += 1
		
		if conta == 0:
			raise Warning(('Ningún producto seleccionado'))
		
		obj_stock = self.env["stock.picking"]
		lineas = []
		lineas2 = []

		for line in self.stock_ids:
			vals= {
				'product_id': line.product_id.id,
				'product_uom_qty': line.cantidad,
				'product_uom': line.product_id.uom_id.id,
				'quantity_done':line.cantidad,
				'name': line.product_id.name,
				'location_dest_id':line.stock_id.id
			}


			lineas.append((0, 0, vals))
			#lineas2.append((0, 0, vals2))
			print(self.almacen_id.in_type_id.default_location_src_id.id)
		values = {
			'partner_id': self.proveedor.id,
			'picking_type_id': self.almacen_id.in_type_id.id,
			'move_type': 'direct',
			'priority': '1',
			'move_lines': lineas,
			'move_line_ids':lineas2,
			'state':'done',
			'location_id': self.locacion_id.id,
			'location_dest_id': self.locacion_id.id
		}
		self.idPick = obj_stock.create(values)
		modiLote = self.env["stock.move.line"].search([('picking_id','=',self.idPick.id)])
		conta = 0
		for v in modiLote:
			v.write({
				'lot_id':self.stock_ids[conta].id,
				'location_dest_id':self.stock_ids[conta].stock_id.id
			})
			conta += 1
		

		self.idPick.button_validate()
		self.write({'state':'ingresado'})
		
