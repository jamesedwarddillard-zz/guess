from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import requests
from twitter.guestimator import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
	entry_list = response_aggregator('#nfpguesses', '')
	summary = len(entry_list)
	return render_template('index.html', summary=summary)

@app.route('/<year>/<month>')
def hello_selected_month(year, month):
	return "How many jobs were added in {}, {}?".format(month, year)

if __name__ == '__main__':
	app.run()
    