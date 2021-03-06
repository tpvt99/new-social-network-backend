# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0053_auto_20170504_0311'),
        ('status', '0027_auto_20170514_1023'),
        ('plustag', '0005_auto_20170514_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plustag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plustag_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('votes', models.PositiveIntegerField(default=0)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustag_status', to='status.Status')),
                ('user_receive_plus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustag_user_receive_plus', to='user.User')),
                ('user_send_plus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustag_user_send_plus', to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='PlustagVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('been_vote', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('plustag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustagvote_plustag', to='plustag.Plustag')),
                ('user_vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plustag_plustagvote_user_vote', to='user.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='plustagvote',
            unique_together=set([('user_vote', 'plustag')]),
        ),
        migrations.AlterUniqueTogether(
            name='plustag',
            unique_together=set([('status', 'plustag_name')]),
        ),
    ]
