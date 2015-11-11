# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0002_punch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='punch',
            options={'verbose_name_plural': 'punches'},
        ),
    ]
