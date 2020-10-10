from flask import Flask, request, jsonify, Blueprint
from flask.wrappers import Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId
from config import conexion



usuario = Blueprint('usuario', __name__)


mongo = PyMongo(conexion())

@usuario.route('/usuario')
def obtenerUsuarios():
    usuarios = mongo.db.usuario.find()
    response = json_util.dumps(usuarios)
    return Response(response, mimetype='application/jason' )
    

@usuario.route('/usuario', methods=['POST'])
def crearUsuario():
    nombre = request.json['nombre']
    password = request.json['password']
    correo = request.json['correo']

    if nombre and correo and password:
        password_cifrado =  generate_password_hash(password)
        id = mongo.db.usuario.insert(
            {
                "nombre": nombre,
                "password": password_cifrado,
                "correo": correo
            }
        )
        response = {
            "id": str(id),
            "nombre": nombre,
            "password": password_cifrado,
            "correo": correo
        }
        return response

    else:
        return not_found()


@usuario.route('/usuario/<id>')
def obtenerUsuario(id):
    usuario = mongo.db.usuario.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(usuario)
    return Response(response, mimetype='application/jason' )

@usuario.route('/usuario/<id>', methods=['DELETE'])
def eliminarUsuario(id):
    mongo.db.usuario.delete_one({'_id': ObjectId(id) })
    response = jsonify({'mensaje': "se ha eliminado el usuario"})
    return response



@usuario.route('/usuario/<id>', methods=['PUT'])
def editarUsuario(id):
    nombre = request.json['nombre']
    password = request.json['password']
    correo = request.json['correo']

    if nombre and correo and password:
        password_cifrado =  generate_password_hash(password)
        mongo.db.usuario.update_one({'_id': ObjectId(id)}, {'$set': {
            'nombre': nombre,
            "password": password,
            "correo": correo

        }})

        response = jsonify({'mensaje': 'El usuario a sido actualizado' })
        return response



@usuario.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'mensaje': 'Recurso no encontrado: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response



if __name__ == "__main__":
    usuario.run(debug=True)