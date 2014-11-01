# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realqa', '0003_auto_20141030_1849'),
    ]

    operations = [
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
