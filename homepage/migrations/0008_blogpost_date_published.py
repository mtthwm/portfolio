# Generated by Django 3.2.9 on 2021-11-19 19:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20211119_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date_published',
            field=models.DateField(default=datetime.datetime(2021, 11, 19, 19, 30, 9, 609602, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
