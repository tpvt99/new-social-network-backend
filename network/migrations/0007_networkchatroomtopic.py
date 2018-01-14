# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20170506_1352'),
        ('network', '0006_auto_20170617_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkChatroomTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='network_networkchatroomtopic_image', to='files.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkchatroomtopic_user', to='network.NetworkAccount')),
            ],
        ),
    ]