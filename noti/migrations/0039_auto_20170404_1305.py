# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-04 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0013_auto_20170402_0141'),
        ('noti', '0038_auto_20170404_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupanotification',
            name='group',
        ),
        migrations.AddField(
            model_name='groupanotification',
            name='groupinvitation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='group.GroupInvitation'),
        ),
    ]
