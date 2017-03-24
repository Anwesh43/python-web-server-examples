from flask import *
app = Flask(__name__)
app.debug = True
@app.route('/hello')
def hello():
    return "hello world"
@app.route('/helloName/<name>')
def helloName(name):
    return 'hello {0}'.format(name)
@app.route('/helloQueries')
def helloPerson():
    print request.args
    return "hello person whose age is {0} and name is {1}".format(request.args["age"],request.args["name"])
@app.route('/postPerson',methods=['POST'])
def postPerson():
    person = request.form
    print person
    return "Person's name is {0} and age is {1}\n".format(person["name"],person["age"])
