from django.db import models

class Pizza(models.Model):
    name = models.CharField(verbose_name='pizza', max_length=100, default='DefaultPizza')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    type = models.CharField(max_length=100, default='brak')
    description = models.CharField(max_length=300, default='skladniki')

    def __str__(self):
        return self.name

