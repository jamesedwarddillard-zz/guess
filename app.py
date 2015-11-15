from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello Jimmy!"

@app.route('/<year>/<month>')
def hello_selected_month(year, month):
	return "How many jobs were added in {}, {}?".format(month, year)

if __name__ == '__main__':
	print (os.environ['APP_SETTINGS'])
	app.run()
    