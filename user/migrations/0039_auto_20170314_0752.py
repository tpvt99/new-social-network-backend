# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0038_info_background_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=user.models.user_profilepic_upload),
        ),
    ]
