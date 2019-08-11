from flask import Flask 
from flask import render_template

app = Flask(__name__)

#Macro es para repetir funciones muchas veces jejeje

@app.route('/')
def index():
	name = 'Bubu'

	return render_template('08-index.html', name = name)

@app.route('/client')
def client():
	list_name = ['Bubu', 'Laura', 'Daniel', 'Missalchicha']

	return render_template('08-client.html', names = list_name)

if __name__ == '__main__': 
	app.run(debug = True)