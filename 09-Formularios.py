from flask import Flask 
from flask import render_template
import forms

app = Flask(__name__)

#Macro es para repetir funciones muchas veces jejeje

@app.route('/')
def index():

	comment_form = forms.CommentForm() 
	name = 'Bubu'

	return render_template('09-index.html', name = name, tittle = "index", form = comment_form)

@app.route('/client')
def client():
	list_name = ['Bubu', 'Laura', 'Daniel', 'Missalchicha']

	return render_template('09-client.html', names = list_name, tittle = "client")

if __name__ == '__main__': 
	app.run(debug = True)