# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0044_auto_20170428_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='profile_pic',
            field=models.ImageField(default='/home/web/static/user.jpeg', null=True, upload_to=user.models.user_profilepic_upload),
        ),
    ]
