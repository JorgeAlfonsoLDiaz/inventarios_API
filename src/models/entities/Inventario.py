from utils.DateFormat import DateFormat

class Inventario():

    def __init__(self, id_articulo=None, usuario_asignado=None, clasificacion=None, marca=None, condicion=None, no_serie=None, modelo=None, fecha_asignacion=None, cantidad=None, otras_especificaciones=None) -> None:
        self.id_articulo = id_articulo
        self.usuario_asignado = usuario_asignado
        self.clasificacion = clasificacion
        self.marca = marca
        self.condicion = condicion
        self.no_serie = no_serie
        self.modelo = modelo
        self.fecha_asignacion = fecha_asignacion
        self.cantidad = cantidad
        self.otras_especificaciones = otras_especificaciones

    def to_JSON(self):
        if self.fecha_asignacion != None:
            self.fecha_asignacion = DateFormat.convert_date(self.fecha_asignacion)
        
        return { 
            'id_articulo': self.id_articulo,
            'usuario_asignado': self.usuario_asignado,
            'clasificacion': self.clasificacion,
            'marca': self.marca,
            'condicion': self.condicion,
            'no_serie': self.no_serie,
            'modelo': self.modelo,
            'fecha_asignacion': self.fecha_asignacion,
            'cantidad': self.cantidad,
            'otras_especificaciones': self.otras_especificaciones
        }
