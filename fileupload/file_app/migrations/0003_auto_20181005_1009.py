# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_auto_20181005_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='description',
        ),
        migrations.RemoveField(
            model_name='file',
            name='timestamp',
        ),
    ]
