# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_remove_cart_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.IntegerField(default=b'0'),
        ),
    ]
