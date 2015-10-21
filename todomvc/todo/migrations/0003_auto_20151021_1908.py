# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20151021_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='task',
            new_name='title',
        ),
    ]
