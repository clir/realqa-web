# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=125)),
                ('added_at', models.DateTimeField(default=datetime.datetime.now)),
                ('score', models.IntegerField(null=True)),
                ('time_spent_editing', models.IntegerField(null=True)),
                ('vote', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('tagnames', models.CharField(max_length=125)),
                ('author', models.CharField(max_length=125)),
                ('added_at', models.DateTimeField(default=datetime.datetime.now)),
                ('score', models.IntegerField(null=True)),
                ('time_spent_editing', models.IntegerField(null=True)),
                ('answer_count', models.IntegerField(null=True)),
                ('vote', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='realqa.Question'),
            preserve_default=True,
        ),
    ]
