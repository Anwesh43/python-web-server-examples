from flask import *
from config import *
from mongoengine import *
from models.Person import *
from daos.ModelDao import *
modelDao = ModelDao()
app = Flask(__name__)
app.debug = True
app.secret_key = secretKey
connect('repdb')
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
@app.route('/setPerson/<string:name>/<int:age>')
def setPerson(name,age):
    if countKey not in session:
        session[countKey] = 0
    nameKey = "{0}-name".format(session[countKey])
    ageKey = "{0}-age".format(session[countKey])
    session[countKey] = session[countKey]+1
    session[nameKey] = name
    session[ageKey] = age
    return 'thanks for adding a person'
@app.route('/getPerson/<int:id>')
def getPerson(id):
    if id >= session[countKey]:
        return "the person you are looking for is not present"
    return render_template('main.html',name=session["{0}-name".format(id)],age=session["{0}-age".format(id)])
@app.route('/newPerson/<string:name>/<int:age>')
def newPerson(name,age):
    modelDao.create(Person,name=name,age=age)
    return "created a new person"
@app.route('/persons')
def getPersons():
    persons  = modelDao.findObjects(Person)
    personStr = ""
    print persons
    return render_template('persons.html',persons=persons)
