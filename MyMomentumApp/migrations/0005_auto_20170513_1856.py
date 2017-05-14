# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMomentumApp', '0004_auto_20170512_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='index',
            field=models.ManyToManyField(to='MyMomentumApp.Index'),
        ),
    ]
