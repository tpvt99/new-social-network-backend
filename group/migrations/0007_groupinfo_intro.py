# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_auto_20170329_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupinfo',
            name='intro',
            field=models.TextField(null=True),
        ),
    ]
