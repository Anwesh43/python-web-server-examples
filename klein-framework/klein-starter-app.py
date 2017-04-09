from klein import route,run

@route('/')
def index(request):
    return "hello world"
@route('/hello/<username>')
def hello(request,username):
    return "hello {0}".format(username)    
run("localhost",8000)
