from flask import Flask, flash, render_template, request
import os
import ttt
from tables import pylist_2_htmltable

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	if request.method == 'POST' and 'count' in request.form:
		n = request.form['count']

		pylist = ttt.give_count(n)[:int(n)]
		pylist_2_htmltable(pylist)

		return render_template('result.html')
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'

	app.run(debug=True)
