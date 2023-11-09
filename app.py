from flask import Flask, redirect, request, jsonify, render_template
from models import db, FormularioContacto, create_tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

# Crea las tablas en la base de datos
with app.app_context():
    create_tables()

# Consulta datos de la tabla
with app.app_context():
    formularios = FormularioContacto.query.all()

    for formulario in formularios:
        print(f"ID: {formulario.id}, Nombre: {formulario.nombre}, Email: {formulario.email}, Edad: {formulario.edad}, Motivo: {formulario.motivo}")


#Manejo de errores

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Solicitud incorrecta"}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404


#Endpoints

@app.route('/ver-datos')
def ver_datos():
    with app.app_context():
        formularios = FormularioContacto.query.all()
    return render_template('ver-datos.html', formularios=formularios)

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

    # Redirigir al usuario a la página /ver-datos después de guardar los datos
    return redirect('/ver-datos')

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
    with app.app_context():
        create_tables()
    app.run(debug=True)


