# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from .models import Pizza

def index(request):
    allPizzas = Pizza.objects.all()

    template = loader.get_template('menu/index.html')
    context = {
        'allPizzas': allPizzas,
    }
    return HttpResponse(template.render(context, request))
