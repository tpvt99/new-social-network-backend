# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0040_auto_20170507_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdnotification',
            name='guess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_eventdnotification_guess', to='user.User'),
        ),
    ]
