# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('One', '0004_auto_20200422_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='g_name',
            field=models.CharField(default=b'', max_length=32, db_column=b'grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_name',
            field=models.CharField(default=b'', max_length=32, db_column=b'name'),
        ),
    ]
