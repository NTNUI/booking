# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-10 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='group',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
