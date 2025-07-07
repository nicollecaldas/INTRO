from flask import Flask, render_template, request, redirect, url_for
from db_config import db
from huecos import huecos  # CORRECCIÓN 1: Importa la CLASE 'Hueco', no solo el módulo

class Programa:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///huecos.sqlite3"
        
        db.init_app(self.app)

        # CORRECCIÓN 2: Es mejor práctica usar nombres de función en minúsculas (snake_case)
        self.app.add_url_rule('/', view_func=self.buscar_todos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=['GET', 'POST'])

        with self.app.app_context():
            db.create_all()
        
        # No es necesario ejecutar self.app.run() aquí si vas a instanciar la clase abajo
        # Se ejecutará al final del script

    def buscar_todos(self):
        # CORRECCIÓN 3: Haz la consulta sobre la CLASE 'Hueco', no sobre el módulo 'huecos'
        todos_los_huecos = huecos.query.all()
        return render_template('listado.html', huecos=todos_los_huecos)

    def agregar(self):
        if request.method == 'POST':
            direccion = request.form['direccion']
            ancho = request.form['ancho']
            profundidad = request.form['profundidad']
            largo = request.form['largo']

            # CORRECCIÓN 4: Crea una instancia de la CLASE 'Hueco'
            mi_hueco = huecos(direccion=direccion, ancho=ancho, profundidad=profundidad, largo=largo)
            db.session.add(mi_hueco)
            db.session.commit()

            # CORRECCIÓN 5: Redirige a la función correcta usando su nombre
            return redirect(url_for('buscar_todos'))

        return render_template('addpoint.html')
    
    def run(self):
        self.app.run(debug=True)

# Así se ejecuta la aplicación
if __name__ == '__main__':
    miPrograma = Programa()
    miPrograma.run()