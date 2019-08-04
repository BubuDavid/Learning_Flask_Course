#http://127.0.0.1:5000/

from flask import Flask 
#Importr render:
from flask import render_template


app = Flask(__name__)

#Todo está en html
@app.route('/')
def user():
	name = 'Bubu'

	return render_template('07-welcome.html', name = name)

@app.route('/client')
def user():
	list_name = ['Bubu', 'Laura', 'Daniel', 'Missalchicha']

	return render_template('07-welcome.html', names = list_name)

if __name__ == '__main__': 
	app.run(debug = True)