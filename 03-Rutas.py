#http://127.0.0.1:5000/

from flask import Flask 
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hola mundo'

#Se conectan con hypervincules.
#Las funciones tienen que ser distintas.
@app.route('/params')
def params():
	#Esto es para los URL de tipo:
	#http://127.0.0.1:8000/params?params1=Bubu
	#Es decir: params?params1=Bubu
	param = request.args.get('params1', 'No existe')
	return 'El parametro es: {}'.format(param)


if __name__ == '__main__': 
	app.run(debug = True, port = 8000)