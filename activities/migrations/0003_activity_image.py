# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]