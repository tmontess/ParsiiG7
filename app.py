from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Ejemplo de una base de datos SQLite
db = SQLAlchemy(app)

# Definir un modelo de datos para la tabla de formularios de contacto
class FormularioContacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    email = db.Column(db.String(120))
    edad = db.Column(db.Integer)
    motivo = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Solicitud incorrecta"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/advanced')
def advanced():
    return render_template('Advanced.html')

@app.route('/enterprise')
def enterprise():
    return render_template('Enterprise.html')

@app.route('/experience')
def experience():
    return render_template('experiencia.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes-somos.html')

@app.route('/starter')
def starter():
    return render_template('starter.html')

@app.route('/contacto')
def contacto():
    return render_template('forms-contacto.html')

@app.route('/api/forms-contacto', methods=['POST'])
def recibir_datos_formscontacto():
    data = request.form
    nuevo_formulario = FormularioContacto(
        nombre=data.get('name'),
        email=data.get('email'),
        edad=data.get('age'),
        motivo=data.get('explanation')
    )

    db.session.add(nuevo_formulario)
    db.session.commit()

    return jsonify({"message": "Datos de forms-contacto recibidos y guardados en la base de datos"})

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def actualizar_cliente(cliente_id):
    # Lógica para actualizar el cliente con el ID proporcionado
    # Utiliza request.json para obtener los datos del cliente a actualizar
    # Implementa la lógica para actualizar el cliente en la base de datos
    return jsonify({"message": "Cliente actualizado con éxito"})

@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def eliminar_cliente(cliente_id):
    # Lógica para eliminar el cliente con el ID proporcionado
    # Implementa la lógica para eliminar el cliente de la base de datos
    return jsonify({"message": "Cliente eliminado con éxito"})

if __name__ == '__main__':
    app.run(debug=True)


