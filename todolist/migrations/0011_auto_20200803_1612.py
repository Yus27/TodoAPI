# Generated by Django 3.0 on 2020-08-03 06:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_auto_20200803_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lastChangeDateTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 6, 12, 26, 513238, tzinfo=utc)),
        ),
    ]
