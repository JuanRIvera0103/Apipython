from  flask import Flask, request, jsonify, Blueprint
# from flask.wrappers import Response
# from flask_pymongo import PyMongo
# from werkzeug.security import generate_password_hash, check_password_hash
# from bson import json_util
# from bson.objectid import ObjectId
# from src.config import conexion

producto = Blueprint('producto', __name__)

@producto.route('/producto')
def obtenerUsuarios():    
    return 'Este es la api con el producto' 
