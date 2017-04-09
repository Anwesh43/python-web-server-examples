from klein import route,run

@route('/')
def index(request):
    return "hello world"
run("localhost",8000)
