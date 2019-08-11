#http://127.0.0.1:5000/

from flask import Flask 
#Importr render:
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
	return "Hello men go to localhost:8000/user/name"

#Todo está en html
@app.route('/user/<name>')
def user(name = "Bubu"):
	age = 18
	my_list1 = [1, 2, 3, 4]

	return render_template('06-user.html', name = name, age = age, lista = my_list)


if __name__ == '__main__': 
	app.run(debug = True, port = 8000)