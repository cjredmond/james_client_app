# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='workout',
        ),
        migrations.AddField(
            model_name='workout',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default='2017-03-30'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]
