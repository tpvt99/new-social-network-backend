# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0028_auto_20170623_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='verb',
            field=models.CharField(max_length=30),
        ),
    ]