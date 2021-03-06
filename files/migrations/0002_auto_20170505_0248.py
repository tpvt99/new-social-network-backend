# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='has_saved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(height_field='image_height', null=True, upload_to=files.models.UploadToPathAndRename('uploads/'), width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
