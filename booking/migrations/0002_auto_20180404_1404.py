# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-04 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='description',
            new_name='title',
        ),
    ]