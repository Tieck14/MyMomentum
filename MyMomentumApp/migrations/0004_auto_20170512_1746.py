# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyMomentumApp', '0003_auto_20170512_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyMomentumApp.Instrument'),
        ),
    ]