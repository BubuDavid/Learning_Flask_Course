#http://127.0.0.1:5000/

from flask import Flask 
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hola mundo'

#Para recibir parámetros sin el signo de intorrogación de este tipo:
#params/libros/1
@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name='Default', num = 'nada'):
	param = request.args.get('params1', 'No existe')
	return 'El parametro es: {}, {}'.format(name, num)

if __name__ == '__main__': 
	app.run(debug = True, port = 8000)