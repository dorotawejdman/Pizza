from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
    url(r'^$', views.index, name='menu'),
    url(r'^(?P<pizza_id>[0-9]+)-(?P<pizza_size>[0-9]{1})$', views.addToCart, name='addToCart'),
]