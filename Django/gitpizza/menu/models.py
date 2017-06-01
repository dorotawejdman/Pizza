from django.db import models

class Ingredient(models.Model):
    name = models.CharField(verbose_name='skladnik', max_length=100, default='Default Ingredient')

class Pizza(models.Model):
    name = models.CharField(verbose_name='pizza', max_length=100, default='DefaultPizza')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    type = models.CharField(max_length=100, default='zwykla')
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="skladnik", null=True)

