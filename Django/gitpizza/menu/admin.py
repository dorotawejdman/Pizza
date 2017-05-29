# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Pizza, Ingredient

admin.site.register(Pizza)
admin.site.register(Ingredient)