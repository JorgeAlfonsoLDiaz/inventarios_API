class Marcas():

    def __init__(self, id_marca, nombre=None, descripcion=None) -> None:
        self.id_marca = id_marca
        self.nombre = nombre
        self.descripcion = descripcion

    def to_JSON(self):
        return { 
            'id_marca': self.id_marca,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }
