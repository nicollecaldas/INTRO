from db_config import db

class huecos(db.Model):

    __tablename__= 'huecos'
    
    id=db.Column(db.Integer, primary_key=True)
    direccion=db.Column(db.String(100))
    ancho=db.Column(db.Float)
    profundidad=db.Column(db.Float)
    largo=db.Column(db.Float)

    def __init__(self, direccion, ancho, profundidad, largo):
        self.direccion = direccion
        self.ancho = ancho
        self.profundidad = profundidad
        self.largo = largo