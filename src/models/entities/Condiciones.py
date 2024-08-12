class Condiciones():

    def __init__(self, id_condicion, condicion=None, descripcion=None) -> None:
        self.id_condicion = id_condicion
        self.condicion = condicion
        self.descripcion = descripcion

    def to_JSON(self):
        return { 
            'id_condicion': self.id_condicion,
            'condicion': self.condicion,
            'descripcion': self.descripcion
        }
