from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Jimmy!"

@app.route('/<year>/<month>')
def hello_selected_month(year, month):
	return "How many jobs were added in {}, {}?".format(month, year)

if __name__ == '__main__':
    app.run()