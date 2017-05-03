#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, render_template
import datetime


app = Flask(__name__, static_url_path = "/static", static_folder = "static")

@app.route('/')
@app.route('/index')
def index():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/puppy1')
def puppy1():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/puppy2')
def puppy2():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/puppy3')
def puppy3():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/kitten1')
def kitten1():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/kitten2')
def kitten2():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

@app.route('/img/kitten3')
def kitten3():
	f = open('workfile', 'a')
	f.write(str(request))
	f.write(str({"newHeader": str(request.headers)}))
	f.write(str(datetime.datetime.now()))
	f.write("\n\n")
	return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
