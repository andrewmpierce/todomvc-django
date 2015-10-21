# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20151021_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='url',
        ),
        migrations.AddField(
            model_name='todo',
            name='order',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
