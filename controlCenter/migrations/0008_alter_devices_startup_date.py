# Generated by Django 3.2.7 on 2021-11-10 22:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('controlCenter', '0007_alter_devices_startup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='startup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 22, 20, 20, 265931, tzinfo=utc)),
        ),
    ]
