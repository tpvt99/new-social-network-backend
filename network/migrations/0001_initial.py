# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0004_auto_20170506_1352'),
        ('user', '0055_auto_20170520_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('birthYear', models.IntegerField()),
                ('nationality', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=10)),
                ('profile_piture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
