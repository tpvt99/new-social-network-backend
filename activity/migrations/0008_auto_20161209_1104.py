# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_auto_20161207_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityparticipants',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activityparticipants_activity', to='activity.Activity'),
        ),
    ]