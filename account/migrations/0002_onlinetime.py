# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_auto_20170520_0237'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
