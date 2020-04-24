# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('One', '0003_auto_20200422_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_name',
            field=models.CharField(max_length=32, db_column=b'name'),
        ),
    ]
