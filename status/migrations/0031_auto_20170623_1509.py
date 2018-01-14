# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0030_status_who_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='who_owner',
            field=models.CharField(default='user', max_length=30),
        ),
        migrations.AddField(
            model_name='status',
            name='who_owner_id',
            field=models.IntegerField(null=True),
        ),
    ]
