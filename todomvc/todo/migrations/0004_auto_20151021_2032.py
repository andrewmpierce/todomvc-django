# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20151021_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True),
        ),
    ]
