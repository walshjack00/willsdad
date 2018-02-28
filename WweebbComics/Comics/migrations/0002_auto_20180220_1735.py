# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-02-20 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percent_take', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comic',
            name='author',
        ),
        migrations.DeleteModel(
            name='Artwork',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Comic',
        ),
    ]
