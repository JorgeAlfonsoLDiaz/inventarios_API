class Empresas():

    def __init__(self, id_empresa, nombre=None, nombre_corto=None, director_general=None, descripcion=None, estatus=None) -> None:
        self.id_empresa = id_empresa
        self.nombre = nombre
        self.nombre_corto = nombre_corto
        self.director_general = director_general
        self.descripcion = descripcion
        self.estatus = estatus

    def to_JSON(self):
        return { 
            'id_empresa': self.id_empresa,
            'nombre': self.nombre,
            'nombre_corto': self.nombre_corto,
            'director_general': self.director_general,
            'descripcion': self.descripcion,
            'estatus': self.estatus
        }
