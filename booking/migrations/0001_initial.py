# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=400)),
                ('description', models.CharField(default='', max_length=400)),
                ('start', models.DateTimeField(blank=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, verbose_name='End')),
                ('group', models.CharField(blank=True, choices=[('', '---------')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('type', models.CharField(choices=[('gym ', 'GYM'), ('football field', 'FOOTBALL FIELD'), ('volleyball grounds', 'VOLLEYBALL GROUNDS')], default='gym', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Location'),
        ),
        migrations.AddField(
            model_name='booking',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
