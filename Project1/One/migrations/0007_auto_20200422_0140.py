# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('One', '0006_auto_20200422_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': '\u73ed\u7ea7', 'verbose_name_plural': '\u73ed\u7ea7'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u5b66\u751f', 'verbose_name_plural': '\u5b66\u751f'},
        ),
    ]
