# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_networkgoal_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkChatFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ManyToManyField(related_name='network_networkchatframe_user', to='network.NetworkAccount')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkChatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=True)),
                ('fetch', models.BooleanField(default=True)),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkchatuser_frame', to='network.NetworkChatFrame')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkchatuser_user', to='network.NetworkAccount')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('chat_frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkmessage_chat_frame', to='network.NetworkChatFrame')),
                ('user_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkmessage_user_send', to='network.NetworkAccount')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkMessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('fetch', models.BooleanField(default=False)),
                ('network_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkmessageinfo_network_message', to='network.NetworkMessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_networkmessageinfo_user', to='network.NetworkAccount')),
            ],
        ),
    ]
