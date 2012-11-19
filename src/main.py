__author__ = 'IGulyaev'

import bottle
from bottle import route, template


@route('/')
@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

def gae_env():
    from google.appengine.ext.webapp.util import run_wsgi_app

    bottle.debug(True)
    run_wsgi_app(bottle.default_app())

def local_env():
    bottle.run(host='localhost', port=8080, debug=True)

if __name__=="__main__":
    local_env()
