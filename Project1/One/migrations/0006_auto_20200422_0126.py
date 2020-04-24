# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('One', '0005_auto_20200422_0117'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='grade',
            table='grade',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
