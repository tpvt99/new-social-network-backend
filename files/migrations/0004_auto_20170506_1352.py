# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20170505_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
