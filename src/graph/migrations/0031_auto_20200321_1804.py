# Generated by Django 2.2 on 2020-03-21 21:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0030_auto_20200321_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participacaopergunta',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 21, 21, 4, 35, 990883, tzinfo=utc)),
        ),
    ]