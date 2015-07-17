from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Name
import requests


def index(request):
    name_list = Name.objects.all()
    template = loader.get_template('alumni/index.html')
    context = RequestContext(request, {
        'name_list': name_list,
    })
    return HttpResponse(template.render(context))

def dataviz(request):
    template = loader.get_template('alumni/dataviz.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def detail(request, name_id):
    try:
        name = Name.objects.get(pk=name_id)
    except Name.DoesNotExist:
        raise Http404("Name does not exist")
    return render(request, 'alumni/detail.html', {'name': name})

def new(request):
    if request.method == 'POST':
        name_text = request.POST['name']
        address_street = request.POST['address_street']
        address_city = request.POST['address_city']
        address_state = request.POST['address_state']
        address_text = address_street + ' ' + address_city + ', ' + address_state

        google_address = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address=' + address_text).json()
        lat = google_address['results'][0]['geometry']['location']['lat']
        lon = google_address['results'][0]['geometry']['location']['lng']

        name = Name(name_text=name_text, address_text=address_text, lat = lat, lon = lon)
        name.save()
        return HttpResponseRedirect(reverse('alumni:index'))
    else:
        template = loader.get_template('alumni/new.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))