# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realqa', '0002_auto_20141030_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
