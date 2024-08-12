class Areas():

    def __init__(self, id_area, nombre=None, descripcion=None, estatus=None) -> None:
        self.id_area = id_area
        self.nombre = nombre
        self.descripcion = descripcion
        self.estatus = estatus

    def to_JSON(self):
        return { 
            'id_area': self.id_area,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estatus': self.estatus
        }
