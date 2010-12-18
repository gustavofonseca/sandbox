from django.shortcuts import render_to_response, redirect
from odclinic.pacient.models import Pacient

def search(request):    
    '''
    Return a list of Pacient objects that match the provided
    search term in name.
    '''
    if 'q' in request.GET:
        pacient_list = Pacient.objects.filter(name__contains = request.GET['q'])
        
    return render_to_response('pacient/pacient_list.html', locals())
    