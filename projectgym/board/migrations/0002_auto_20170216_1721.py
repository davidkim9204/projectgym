# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='post',
            name='effect',
            field=models.TextField(verbose_name='효과'),
        ),
    ]
