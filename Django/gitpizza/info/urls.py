from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^o-nas$', views.onas, name='onas'),
    url(r'^o-projekcie$', views.oprojekcie, name='oprojekcie'),
]