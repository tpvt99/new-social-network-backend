# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_activitypostcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitypost',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
