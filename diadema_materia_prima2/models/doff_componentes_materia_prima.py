# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Origen(models.Model):
	_name = "doff.origen.materia"

	name = fields.Char("Origen", required=True)
	codigo_origen = fields.Char("Código", required=True)
	zona_ids = fields.One2many("doff.zona.origen","origen_id")


	_sql_contraints = [('codigo_origen','unique(codigo_origen)','El código debe ser único')]

class MateriaPrima(models.Model):
	_name = "doff.tipo.materia"

	name = fields.Char("Tipo de materia prima", required=True)
	codigo_materia = fields.Char("Código", required=True)
	semilla_ids = fields.One2many("doff.semilla","tipo_materia_id")

	_sql_contraints = [('codigo_materia','unique(codigo_materia)','El código debe ser único')]

class Grado(models.Model):
	_name = "doff.grado"

	name = fields.Char("Grado", required=True)
	codigo_gado = fields.Char("Código", required=True)


	_sql_contraints = [('codigo_gado','unique(codigo_gado)','El código debe ser único')]

class Corte(models.Model):
	_name = "doff.corte"

	name = fields.Char("Corte", required=True)
	codigo_corte = fields.Char("Código", required=True)


	_sql_contraints = [('codigo_corte','unique(codigo_corte)','El código debe ser único')]

class Size(models.Model):
	_name = "doff.size"

	name = fields.Char("Tamaño", required=True)
	codigo_size = fields.Char("Código", required=True)


	_sql_contraints = [('codigo_size','unique(codigo_size)','El código debe ser único')]

class Zona(models.Model):
	_name = "doff.zona.origen"

	name = fields.Char("Zona", required=True)
	codigo_zona = fields.Char("Código", required=True)
	origen_id = fields.Many2one("doff.origen.materia","Origen")


	_sql_contraints = [('codigo_zona','unique(codigo_zona)','El código debe ser único')]


class Semilla(models.Model):
	_name = "doff.semilla"

	name = fields.Char("Semilla", required=True)
	codigo_seed = fields.Char("Código", required=True)
	tipo_materia_id = fields.Many2one("doff.tipo.materia","Tipo")


	_sql_contraints = [('codigo_seed','unique(codigo_seed)','El código debe ser único')]

class Estado(models.Model):
	_name = "doff.estado"

	name = fields.Char("Estado", required=True)
	codigo_estado = fields.Char("Código", required=True)


	_sql_contraints = [('codigo_estado','unique(codigo_estado)','El código debe ser único')]