# -*- coding: utf-8 -*-

from odoo import models, fields, api


class quatation(models.Model):
    _name = 'quatation.quatation'
    _description = 'quatation.quatation'

    name = fields.Char(string="Order ID")
    cadrs = fields.Char(string="Customer address")
    cph = fields.Char(string="Customer Phone Number")
    orderid = fields.One2many('orderids.orderids','oid',string='Order Details')
    prdlist =fields.Many2many('products1.products1','plist',string='Custmor')

class bill(models.Model):
    _name = 'orderids.orderids'

    oid = fields.Many2one('quatation.quatation',string='Order ID')
    pname = fields.Char(sting='Product Name')
    quantity = fields.Integer(sting="Quantity")
    pbrand = fields.Char(sting='Product Brand')

class product(models.Model):
    _name='products1.products1'

    plist = fields.Many2many('quatation.quatation', string="Product ID")
    pno =fields.Integer(string="Total quantity")
