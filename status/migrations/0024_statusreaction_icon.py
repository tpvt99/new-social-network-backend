# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0023_remove_status_has_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusreaction',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
