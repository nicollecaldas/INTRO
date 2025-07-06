from flask import Flask, render_template, request, redirect, url_for
from db_config import db
from huecos import huecos

class Programa:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///huecos.sqlite3"

        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=['GET', 'POST'])

        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)

    def buscarTodos(self):
        return render_template('mostrarTodos.html', huecos=huecos.query.all())
    def agregar(self):

        if request.method == 'POST':
            direccion = request.form['direccion']
            ancho = request.form['ancho']
            profundidad = request.form['profundidad']
            largo = request.form['largo']

            mihueco = huecos(direccion, ancho, profundidad, largo)
            db.session.add(mihueco)
            db.session.commit()

            return redirect(url_for('buscarTodos'))

        return render_template('addpoint.html')

miPrograma = Programa()