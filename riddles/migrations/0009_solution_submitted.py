# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0008_info_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]