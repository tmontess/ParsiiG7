from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static')


# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de clientes
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

# Rutas para otras páginas
@app.route('/advanced')
def advanced():
    return render_template('Advanced.html')

@app.route('/enterprise')
def enterprise():
    return render_template('Enterprise.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes-somos.html')

@app.route('/starter')
def starter():
    return render_template('starter.html')

# Ruta para el formulario de contacto
@app.route('/contacto')
def contacto():
    return render_template('forms-contacto.html')


@app.route('/api/forms-contacto', methods=['POST'])
def recibir_datos_formscontacto():
    # Obtiene los datos del formulario enviados a través de la solicitud POST.
    data = request.form

    # Procesa y almacena los datos en el diccionario de datos de forms-contacto.
    datos_formscontacto = {
        'nombre': data.get('name'),
        'email': data.get('email'),
        'edad': data.get('age'),
        'motivo': data.get('explanation')
    }

    # Devuelve una respuesta exitosa como JSON.
    print(datos_formscontacto)
    return jsonify({"message": "Datos de forms-contacto recibidos con éxito"})

if __name__ == '__main__':
    app.run(debug=True)



