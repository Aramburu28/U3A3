from odoo import api, models, fields




class Dueno(models.Model):
    _name = 'salesianos.dueno'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    mascota = fields.Many2one(comodel_name='salesianos.mascota', string='mascota') # relacion con el modelo vendedor comodel es el modelo con el que se relaciona, string es el nombre que se le da a la relacion
    edad = fields.Integer()
    edad2 = fields.Integer()
    sumar = fields.Integer(compute='_sumar', store=True) # el campo imc es calculado y se almacena en la base de datos
    @api.depends('edad', 'edad2') # dependencias del campo imc
    def _sumar(self):
        for record in self:
            record.sumar = (record.edad + record.edad2) / 2
    tienda = fields.Many2many(comodel_name='salesianos.tienda', string='tienda')
    # restricción de campos en el modelo @api.constraints añade un decorador (for record in self) cuando se crea un objeto, los datos se guardan en self -> record, en realidad no es un bucle, solo se ejecuta una vez; el registro que se está guardando en ese momento. El record es el objeto que se está guardando de la clase cliente, poniendo el .edad se accede al campo edad y si se quiere acceder a más campos hay que ponerlos en la lista, @api.constraints('edad', 'nombre', ...)



class Mascota(models.Model):
    _name = 'salesianos.mascota'
    name = fields.Char(required=True)
    especie = fields.Char()
    raza = fields.Char()
    fecha_nacimiento = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.dueno', inverse_name='mascota') # relacion con el modelo cliente, inverse_name es el campo que se relaciona con el modelo cliente (vendedor en este caso) y comodel_name es el modelo con el que se relaciona (cliente en este caso)
    curioso = fields.Selection(selection=[('Si', 'No'), ('No', 'Si')])
class Tienda(models.Model):
    _name = 'salesianos.tienda'
    name = fields.Char(required=True)
    cliente = fields.Many2many(comodel_name='salesianos.dueno', string='cliente')
class Herencia(models.Model):
    _inherit = 'base.empresa'
    _name = 'salesianos.herencia'

