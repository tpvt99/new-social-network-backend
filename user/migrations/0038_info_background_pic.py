# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_auto_20170128_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='background_pic',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
