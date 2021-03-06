# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 19:06
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('Ru', 'Ru'), ('Es', 'Es')], default='Es', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/tmp/'), upload_to='')),
                ('text', models.TextField(blank=True, default='')),
            ],
        ),
    ]
