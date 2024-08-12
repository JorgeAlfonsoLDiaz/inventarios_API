from marshmallow import Schema, fields, validate

class MarcaSchema(Schema):
    id_marca = fields.Int(required=False)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=25))
    descripcion = fields.Str(required=True, validate=validate.Length(min=1, max=120))
