# Generated by Django 3.0 on 2020-08-03 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_auto_20200803_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lastChangeDateTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 15, 59, 51, 538628)),
        ),
    ]
