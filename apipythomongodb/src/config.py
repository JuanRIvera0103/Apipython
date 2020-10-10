
from  flask import Flask
from flask_pymongo import PyMongo

def conexion():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost/pythonmongodb'
    
    return app