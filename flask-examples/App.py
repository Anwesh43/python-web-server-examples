from flask import *
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "hello world"
@app.route('/helloName/<name>')
def helloName(name):
    return 'hello {0}'.format(name)
