# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MateriaCigars(models.Model):
	_inherit = "product.product"

	tipo_materia_id = fields.Many2one("doff.tipo.materia", "Tipo de materia prima")
	grado_id = fields.Many2one("doff.grado", "Grado")
	corte_id = fields.Many2one("doff.corte", "Corte")
	size_id = fields.Many2one("doff.size", "Tamaño")
	origen_id = fields.Many2one("doff.origen.materia", "Origen")
	zona_id = fields.Many2one("doff.zona.origen", "Zona")
	semilla_id = fields.Many2one("doff.semilla", "Semilla")
	estado_id = fields.Many2one("doff.estado", "Estado")
	materia = fields.Boolean("Materia Prima")
	brand_id = fields.Many2one("doff.brand.cigars", "Marca")
	vitola_id = fields.Many2one("doff.category.size.line", "Vitola")
	description_id = fields.Many2one("doff.description.desnudo", "Descripción")
	diadema = fields.Boolean("Diadema")
	code_diadema = fields.Char("Código Diadema")

	@api.one
	def set_code_diadema(self):
		if self.diadema:
			code = str(self.brand_id.codigo_brand) + "-" + str(self.description_id.codigo_description) + "-" + str(self.vitola_id.size_articles)
			self.code_diadema = code

	
	@api.one
	def set_code(self):
		if self.materia:
			code = str(self.tipo_materia_id.codigo_materia) + "-" + str(self.semilla_id.codigo_seed) + "-" + str(self.corte_id.codigo_corte) + "-" + str(self.size_id.codigo_size) + "-" + str(self.estado_id.codigo_estado) + "-" + str(self.grado_id.codigo_gado) + "-" + str(self.origen_id.codigo_origen) + "-" + str(self.zona_id.codigo_zona)
			self.default_code = code



	









