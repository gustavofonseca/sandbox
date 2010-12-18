from django.conf.urls.defaults import *
from gallery.items.models import Item, Photo

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        kwargs = {
            'template': 'index.html',
            'extra_context': {'item_list': lambda: Item.objects.all()}
        },
        name = 'index'
    ),
    url(r'^items/$', 'django.views.generic.list_detail.object_list',
        kwargs = {
            'queryset': Item.objects.all(),
            'template_name': 'items_list.html',
            'allow_empty': True
        },
        name = 'item_list'
    ),
    url(r'^items/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail',
        kwargs = {
            'queryset': Item.objects.all(),
            'template_name': 'items_detail.html'
        },
        name = 'item_detail'
    ),
    url(r'^photos/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail',
        kwargs = {
            'queryset': Photo.objects.all(),
            'template_name': 'photos_detail.html'
        },
        name = 'photo_detail'
    ),
    # this must be used only in development environment!!
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/gustavofonseca/Projects/gcode/gallery'}),
)