from db_config import db

# Asegúrate de que la clase se llama Hueco (con H mayúscula)
class Hueco(db.Model):
    # ... (el resto del código de tu modelo está bien)
    __tablename__ = 'huecos'
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(255), nullable=False)
    ancho = db.Column(db.Float)
    profundidad = db.Column(db.Float)
    largo = db.Column(db.Float)

    def __init__(self, direccion, ancho, profundidad, largo):
        self.direccion = direccion
        self.ancho = ancho
        self.profundidad = profundidad
        self.largo = largo