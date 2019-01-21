# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Brand(models.Model):
	_name = 'doff.brand.cigars'

	name = fields.Char("Marca", required=True)
	codigo_brand = fields.Char("Código", required=True)
	descripcion_ids = fields.One2many("doff.description.desnudo","brand_id")

	_sql_contraints = [('codigo_brand','unique(codigo_brand)','El código debe ser único')]

class Description(models.Model):
	_name = "doff.description.desnudo"

	name = fields.Char("Descripción", required=True)
	codigo_description = fields.Char("Código", required=True)
	brand_id = fields.Many2one("doff.brand.cigars","Brand")

	_sql_contraints = [('codigo_description','unique(codigo_description)','El código debe ser único')]

class Size(models.Model):
	_name = "doff.size.desnudo"

	name = fields.Char("Tamaño del cigarro", required=True)
	codigo_size = fields.Char("Codigo", required=True)

	_sql_contraints = [('codigo_size','unique(codigo_size)','El código debe ser único')]
	
		