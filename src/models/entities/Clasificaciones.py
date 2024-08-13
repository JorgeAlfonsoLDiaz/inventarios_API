class Clasificaciones():

    def __init__(self, id_clasificacion=None, categoria=None, nombre=None, descripcion=None, estatus=None) -> None:
        self.id_clasificacion = id_clasificacion
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.estatus = estatus

    def to_JSON(self):
        return { 
            'id_clasificacion': self.id_clasificacion,
            'categoria': self.categoria,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estatus': self.estatus,
        }
