from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid_formalchemy.resources import Models
from pyramid.security import Allow, Authenticated, ALL_PERMISSIONS, Everyone
from fatest.models import initialize_sql
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.authentication import RemoteUserAuthenticationPolicy

class ModelsWithACL(Models):
    """A factory to override the default security setting"""
    __acl__ = [
            (Allow, Everyone, ALL_PERMISSIONS),]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'fatest:static')
    config.add_route('home', '/', view='fatest.views.my_view',
                     view_renderer='templates/mytemplate.pt')

    # configure the security stuff
    config = Configurator(settings=settings,
                          authentication_policy=RemoteUserAuthenticationPolicy(),
                          authorization_policy=ACLAuthorizationPolicy())


    # pyramid_formalchemy's configuration
    config.include('pyramid_formalchemy')
    config.include('fa.jquery')
    config.formalchemy_admin('admin',
                             package='fatest',
                             view='fa.jquery.pyramid.ModelView',
                             factory=ModelsWithACL,)

    return config.make_wsgi_app()


