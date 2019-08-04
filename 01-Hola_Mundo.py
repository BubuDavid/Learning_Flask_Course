from flask import Flask 

# Necesitamos una instancia.
# Un nuevo objeto
app = Flask(__name__)

#A qué ruta el cliente puede acceder:
#Decoramos la función app con route que recibe como
#parámetro a dónde el usuario puede entrar
@app.route('/')
#La función sólo regresará un string
def index():
	return 'Hola mundo'

#.run() se encarga de ejecutar el servidor por Default
#en el puerto 5000
app.run()