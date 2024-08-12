from marshmallow import Schema, fields, validate

class MarcaSchema(Schema):
    id_marca = fields.Int(required=False)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=25))
    descripcion = fields.Str(required=False, validate=validate.Length(min=1, max=120))

class CondicionSchema(Schema):
    id_condicion = fields.Int(required=False)
    condicion = fields.Str(required=False, validate=validate.Length(min=1, max=40))
    descripcion = fields.Str(required=True, validate=validate.Length(min=1, max=120))

class CategoriaSchema(Schema):
    id_categoria = fields.Int(required=False)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    descripcion = fields.Str(required=False, validate=validate.Length(min=1, max=120))
    estatus = fields.Bool(required=True)

class AreaSchema(Schema):
    id_area = fields.Int(required=False)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=60))
    descripcion = fields.Str(required=False, validate=validate.Length(min=1, max=120))
    estatus = fields.Bool(required=True)

class EmpresaSchema(Schema):
    id_empresa = fields.Int(required=False)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=90))
    nombre_corto = fields.Str(required=False, validate=validate.Length(min=1, max=10))
    director_general = fields.Str(required=False, validate=validate.Length(min=1, max=40))
    descripcion = fields.Str(required=False, validate=validate.Length(min=1, max=120))
    estatus = fields.Bool(required=True)

class UsuarioSchema(Schema):
    id_usuario = fields.Int(required=False)
    id_empresa = fields.Int(required=True)
    area = fields.Int(required=True)
    puesto = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=40))
    apellido_materno = fields.Str(required=False, validate=validate.Length(min=1, max=30))
    apellido_paterno = fields.Str(required=False, validate=validate.Length(min=1, max=30))

class ClasificacionSchema(Schema):
    id_clasificacion = fields.Int(required=False)
    categoria = fields.Int(required=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    descripcion = fields.Str(required=False, validate=validate.Length(min=1, max=120))
    estatus = fields.Bool(required=True)

class InventarioSchema(Schema):
    id_articulo = fields.Int(required=False)
    usuario_asignado = fields.Int(required=False)
    clasificacion = fields.Int(required=True)
    marca = fields.Int(required=True)
    condicion = fields.Int(required=True)
    no_serie = fields.Str(required=False, validate=validate.Length(min=1, max=15))
    modelo = fields.Str(required=False, validate=validate.Length(min=1, max=25))
    fecha_asignacion = fields.Date(required=False)
    cantidad = fields.Int(required=True)
    otras_especificaciones = fields.Str(required=False, validate=validate.Length(min=1, max=120))
