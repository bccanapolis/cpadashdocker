# Generated by Django 2.2 on 2020-03-22 01:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0031_auto_20200321_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='perguntasegmento',
            name='ano',
            field=models.IntegerField(choices=[(2019, 2019)], default=2020),
        ),
        migrations.AlterField(
            model_name='participacaopergunta',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 22, 1, 53, 25, 102034, tzinfo=utc)),
        ),
    ]