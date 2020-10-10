from  flask import Flask

from entidades.usuario import usuario
from entidades.producto import producto

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'esto es la pagina de inicio'

app.register_blueprint(usuario)
app.register_blueprint(producto)

if __name__ == "__main__":
    app.run(debug=True)