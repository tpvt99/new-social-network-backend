# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20160915_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='sex',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
