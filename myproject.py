#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, render_template

app = Flask(__name__, static_url_path = "/static", static_folder = "static")

@app.route('/')
@app.route('/index')
def index():
	print(request)
	f = open('workfile', 'a')
	f.write(str({"newHeader": str(request.headers)}))
	return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
