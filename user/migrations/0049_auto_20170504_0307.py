# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_auto_20170503_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default='2ebc0b18df2a400db8b2455fbda6fb18', editable=False, unique=True),
        ),
    ]
