# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0002_auto_20170403_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='day',
            new_name='name',
        ),
    ]