from utils.DateFormat import DateFormat

class InventarioLista():

    def __init__(self, id_articulo=None, usuario_asignado=None, puesto=None, fecha_asignacion=None, tipo=None, marca=None, modelo=None, condicion=None, cantidad=None) -> None:
        self.id_articulo = id_articulo
        self.usuario_asignado = usuario_asignado
        self.puesto = puesto
        self.fecha_asignacion = fecha_asignacion
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.condicion = condicion
        self.cantidad = cantidad

    def to_JSON(self):
        if self.fecha_asignacion != None:
            self.fecha_asignacion = DateFormat.convert_date(self.fecha_asignacion)
        
        return { 
            'id_articulo': self.id_articulo,
            'usuario_asignado': self.usuario_asignado,
            'puesto': self.puesto,
            'fecha_asignacion': self.fecha_asignacion,
            'tipo': self.tipo,
            'marca': self.marca,
            'modelo': self.modelo,
            'condicion': self.condicion,
            'cantidad': self.cantidad
        }
