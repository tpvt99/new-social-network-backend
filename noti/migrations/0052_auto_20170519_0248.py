# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0051_auto_20170519_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusbnotification',
            name='statuscomment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='status.StatusComment'),
        ),
    ]