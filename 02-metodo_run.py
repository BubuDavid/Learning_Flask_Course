#http://127.0.0.1:5000/

from flask import Flask 

app = Flask(__name__)


@app.route('/')
#La función sólo regresará un string
def index():
	return 'Hola mundo, whats up'

#El método run(), usa como puerto default el 5000
#Pero podemos cambiar el puerto con el atributo
#port
#Si debug = False no le permite a mi programa
#estar al tanto de cualquier cambio en mi proyecto
if __name__ == '__main__': #Para saber si fue ejecutado directamente o por un tercero
	app.run(debug = True, port = 8000)