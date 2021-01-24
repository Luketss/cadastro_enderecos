from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Endereco

def index(request):
    adress_list = Endereco.objects.order_by('cep')
    template = loader.get_template('website/index.html')
    context = {
        'adress_list': adress_list
    }
    return HttpResponse(template.render(context, request))

