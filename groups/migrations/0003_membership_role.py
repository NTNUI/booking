# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_membership_in_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='role',
            field=models.CharField(default='Member', max_length=30),
            preserve_default=False,
        ),
    ]
