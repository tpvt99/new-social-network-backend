# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0015_activitycomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitycomment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]