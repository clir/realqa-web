# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realqa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='time_spent_editing',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time_spent_editing',
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote',
        ),
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
