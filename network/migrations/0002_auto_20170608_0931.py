# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkaccount',
            old_name='profile_piture',
            new_name='profile_picture',
        ),
    ]
