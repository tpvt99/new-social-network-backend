# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 06:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activities', '0055_auto_20161127_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityseries',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
