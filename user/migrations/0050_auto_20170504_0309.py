# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0049_auto_20170504_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default='fbea16509952492f91511276422f83de', editable=False, unique=True),
        ),
    ]