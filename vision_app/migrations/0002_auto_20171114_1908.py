# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='language',
            field=models.CharField(choices=[('', ''), ('Ru', 'Ru'), ('Es', 'Es')], default='', max_length=5),
        ),
    ]