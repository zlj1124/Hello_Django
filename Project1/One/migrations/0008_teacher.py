# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('One', '0007_auto_20200422_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_name', models.CharField(max_length=32, null=True)),
                ('t_grade', models.ManyToManyField(to='One.Grade', null=True)),
            ],
            options={
                'db_table': 'teacher',
                'verbose_name': '\u8001\u5e08',
                'verbose_name_plural': '\u8001\u5e08',
            },
        ),
    ]
