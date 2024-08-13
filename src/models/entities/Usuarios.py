class Usuarios():

    def __init__(self, id_usuario=None, empresa=None, area=None, puesto=None, nombre=None, apellido_paterno=None, apellido_materno=None) -> None:
        self.id_usuario = id_usuario
        self.empresa = empresa
        self.area = area
        self.puesto = puesto
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

    def to_JSON(self):
        return { 
            'id_usuario': self.id_usuario,
            'empresa': self.empresa,
            'area': self.area,
            'puesto': self.puesto,
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno
        }
