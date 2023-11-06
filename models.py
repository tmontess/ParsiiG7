from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir un modelo de datos para la tabla de formularios de contacto
class FormularioContacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    email = db.Column(db.String(120))
    edad = db.Column(db.Integer)
    motivo = db.Column(db.String(200))

# Crear las tablas en la base de datos
def create_tables():
    db.create_all()

