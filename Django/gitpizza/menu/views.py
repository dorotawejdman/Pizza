# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from .models import Pizza, Cart
from django.shortcuts import render, redirect

def index(request):
    allPizzas = Pizza.objects.all()
    cart = Cart.objects.all()

    template = loader.get_template('menu/index.html')
    context = {
        'allPizzas': allPizzas,
        'cart': cart,
    }
    return HttpResponse(template.render(context, request))

def addToCart(request, pizza_id, pizza_size):
    pizza = Pizza.objects.get(pk=pizza_id)
    newItem = Cart(pizzaId=pizza, size=pizza_size)
    newItem.save()
    return redirect('menu') 