from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
	errors = []
	results = {}
	if request.method == 'POST':
		try:
			url = request.form['url']
			r = requests.get(url)
			print r.text
		except:
			errors.append(
				"Unable to get URL. Please make sure it's valid and try again"
				)
	return render_template('index.html', errors=errors, results=results)

@app.route('/<year>/<month>')
def hello_selected_month(year, month):
	return "How many jobs were added in {}, {}?".format(month, year)

if __name__ == '__main__':
	app.run()
    