# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_auto_20170127_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
