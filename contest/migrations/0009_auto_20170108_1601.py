# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_contestpostcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestpostcomment',
            name='contestpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_contestpostcomment_contestpost', to='contest.ContestPost'),
        ),
    ]