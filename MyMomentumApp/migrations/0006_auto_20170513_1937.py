# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMomentumApp', '0005_auto_20170513_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='MomentumKPIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slope_float', models.FloatField(default=-1, verbose_name='slope')),
                ('r2_float', models.FloatField(default=-1, verbose_name='r2')),
                ('momentum_float', models.FloatField(default=-1, verbose_name='momentum')),
                ('rank_integer', models.IntegerField(default=-1, verbose_name='rank')),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('number_of_members', models.IntegerField(default=-1, verbose_name='number of members')),
            ],
        ),
        migrations.AddField(
            model_name='index',
            name='number_of_constituents_integer',
            field=models.IntegerField(default=-1, verbose_name='number of constituents'),
        ),
        migrations.AddField(
            model_name='price',
            name='adj_close_float',
            field=models.FloatField(default=-1, verbose_name='adj. close price'),
        ),
        migrations.AddField(
            model_name='price',
            name='high_float',
            field=models.FloatField(default=-1, verbose_name='high price'),
        ),
        migrations.AddField(
            model_name='price',
            name='low_float',
            field=models.FloatField(default=-1, verbose_name='low price'),
        ),
        migrations.AddField(
            model_name='price',
            name='open_float',
            field=models.FloatField(default=-1, verbose_name='open price'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='name_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='symbol_text',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='close_float',
            field=models.FloatField(default=-1, verbose_name='close price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='date_date',
            field=models.DateTimeField(default=-1, verbose_name='date'),
        ),
        migrations.AddField(
            model_name='momentumkpis',
            name='universe',
            field=models.ManyToManyField(to='MyMomentumApp.Universe'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='kpis',
            field=models.ManyToManyField(to='MyMomentumApp.MomentumKPIs'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='universe',
            field=models.ManyToManyField(to='MyMomentumApp.Universe'),
        ),
    ]
