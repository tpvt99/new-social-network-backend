# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0034_auto_20160920_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('icon', models.CharField(max_length=10)),
                ('icon_description', models.CharField(max_length=100)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='moreinfo',
            name='icon',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='moreinfo',
            name='icon_description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moreinfo',
            name='name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]