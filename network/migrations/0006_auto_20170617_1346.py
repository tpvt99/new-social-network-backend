# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 13:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_networkchatframe_networkchatuser_networkmessage_networkmessageinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkchatframe',
            old_name='user',
            new_name='users',
        ),
    ]
