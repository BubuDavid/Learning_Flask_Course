#http://127.0.0.1:5000/

from flask import Flask 
#Importr render:
from flask import render_template

#Para cambiar el nombre de la carpeta de Templates
app = Flask(__name__, template_folder = "Templates")

#Renderizar un archivo HTML

@app.route('/')
def index():
	return render_template('05-Index.html')


if __name__ == '__main__': 
	app.run(debug = True)