# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0047_auto_20170502_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default='e7a75e5bdc6a4f10ba51322ee0f70d61', editable=False, unique=True),
        ),
    ]
