from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)