from django.shortcuts import render, HttpResponse
from django.template import RequestContext, loader

from reports.models import Bandwidth, Graph

def index(request):
    #(used, quota) = Bandwidth.objects.get_all()
    used, quota = (1,2)
    template = loader.get_template('reports/index.html')
    context = RequestContext(request, {
        'used': used,
        'quota': quota,
    })
    return HttpResponse(template.render(context))

def bandwidth(request):
    return HttpResponse('bandwidth stats')

def graph(request):
    return HttpResponse('graph stats')
