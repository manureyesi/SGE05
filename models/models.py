# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):

    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

# INICIO CAMBIOS TAREA SXE05

class Aula(models.Model):

    _name = 'scle.aula'

    centro = fields.Char(string="Centro")
    numAsientos = fields.Integer()
    nombre = fields.Char(string="NombreAula")
    planta = fields.Integer()
    numAula = fields.Integer()

class Partner(models.Model):

    _inherit = 'res.partner'

    esAlumno = fields.Boolean()
    fechaCumpleanos = fields.Date()

# FIN CAMBIOS TAREA SXE05