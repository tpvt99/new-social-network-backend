# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0053_auto_20170504_0311'),
        ('status', '0019_auto_20170503_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reactionName', models.CharField(max_length=30)),
                ('vote', models.IntegerField(default=0)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_statusreaction_status', to='status.Status')),
            ],
        ),
        migrations.CreateModel(
            name='StatusReactionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('been_vote', models.BooleanField(default=False)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('statusreaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_statusreactionvote_statusreaction', to='status.StatusReaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_statusreactionvote_user', to='user.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='statusreactionvote',
            unique_together=set([('user', 'statusreaction')]),
        ),
    ]
