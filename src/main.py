__author__ = 'IGulyaev'

from bottle import route, template, run

@route('/')
@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

def gae_env():
    """ Starts new Bottle instance using GAE adapter """
    run(server='gae', debug=True)

def local_env():
    """ Starts standalone Bottle application (i.e. without GAE backend) """
    run(host='localhost', port=8080, debug=True)

if __name__=="__main__":
    local_env()
