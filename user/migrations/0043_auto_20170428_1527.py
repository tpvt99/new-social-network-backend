# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20170428_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
