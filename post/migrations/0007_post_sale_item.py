# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-24 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20170504_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sale_item',
            field=models.CharField(max_length=100, null=True),
        ),
    ]