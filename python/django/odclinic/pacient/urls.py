from django.conf.urls.defaults import *
from odclinic.pacient.models import Pacient

dict_list_pacients = {'queryset': Pacient.objects.all(), 'template_object_name': 'pacient'}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', dict_list_pacients, name="pacient-list"),
    url(r'^details/(?P<object_id>[\d]+)/$', 'object_detail', dict_list_pacients, name="pacient-detail"),    
)

urlpatterns += patterns('odclinic.pacient.views',
    url(r'^search/$', 'search', name='pacient-search'),
)