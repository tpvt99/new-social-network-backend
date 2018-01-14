# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 09:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noti', '0004_eventbnotification_eventcnotification_eventdnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdnotification',
            name='guess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_eventdnotification_guess', to=settings.AUTH_USER_MODEL),
        ),
    ]
