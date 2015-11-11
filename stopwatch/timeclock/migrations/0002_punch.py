# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timeclock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True, blank=True)),
                ('note', models.CharField(max_length=200, null=True, blank=True)),
                ('project', models.ForeignKey(to='timeclock.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
