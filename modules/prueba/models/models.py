# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

class prueba(models.Model):
    _name = "prueba.proyecto"
    _description = "Prueba"
    name = fields.Char(string="name", required = True) 
    edad = fields.Char(string="edad", required = True)

