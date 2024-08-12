class Categorias():

    def __init__(self, id_categoria, nombre=None, descripcion=None, estatus=None) -> None:
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.estatus = estatus

    def to_JSON(self):
        return { 
            'id_categoria': self.id_categoria,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estatus': self.estatus
        }
