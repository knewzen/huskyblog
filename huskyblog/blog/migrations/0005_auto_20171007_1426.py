# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171007_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m'),
        ),
    ]
