# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

def onas(request):
    template = loader.get_template('info/o-nas.html')
    context = {}
    return HttpResponse(template.render(context, request))

def oprojekcie(request):
    template = loader.get_template('info/o-projekcie.html')
    context = {}
    return HttpResponse(template.render(context, request))