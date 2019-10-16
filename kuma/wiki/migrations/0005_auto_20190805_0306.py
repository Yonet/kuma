# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-05 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0008_auto_20190914_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcsignal',
            name='browsers',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bcsignal',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='bcsignal',
            name='feature',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bcsignal',
            name='supporting_material',
            field=models.TextField(blank=True, default=''),
        ),
    ]
