# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20151021_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True),
        ),
    ]
