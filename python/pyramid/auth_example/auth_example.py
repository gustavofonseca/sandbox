# coding:utf-8
from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import remember
from pyramid.url import route_url
from pyramid.httpexceptions import HTTPFound

USERS = {'admin':'admin'}
GROUPS = {'admin':['group:admin']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])

class Root(object):
    __acl__ = [ (Allow, 'group:admin', ALL_PERMISSIONS) ]

    def __init__(self, request):
        self.request = request

@view_config(route_name='free_access')
def free_access(request):
    return Response('Everyone can see this!')

@view_config(route_name='need_view_access', permission='view')
def need_view_access(request):
    return Response('Need "view" permission to see this!')

@view_config(route_name='login', renderer='login.mako')
def login(request):    
    next = request.params.get('next') or route_url('need_view_access', request)
    login = ''
    did_fail = False
    if 'submit' in request.POST:
        login = request.POST.get('login', '')
        passwd = request.POST.get('passwd', '')
        
        if USERS.get(login) == passwd:
            headers = remember(request, login)
            return HTTPFound(location=next, headers=headers)
        did_fail = True

    return {
        'login': login,
        'next': next,
        'failed_attempt': did_fail,
    }
        
if __name__ == '__main__':
    authe_policy = AuthTktAuthenticationPolicy('seekrit', callback=groupfinder)
    autho_policy = ACLAuthorizationPolicy()
    
    settings = {     
        'mako.directories': '%s:templates' % __name__,
    }

    config = Configurator(settings=settings,
    					  authentication_policy=authe_policy,
                          authorization_policy=autho_policy,
                          root_factory=Root)

    config.add_route('free_access', '/free')
    config.add_route('need_view_access', '/view')
    config.add_route('login', '/login')
    config.scan('__main__')

    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0:6543')