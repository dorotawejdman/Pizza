# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170603_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Pizza')),
            ],
        ),
    ]
