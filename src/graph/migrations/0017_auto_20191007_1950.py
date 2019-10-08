# Generated by Django 2.2.6 on 2019-10-07 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0016_auto_20191007_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='atuacao',
        ),
        migrations.AddField(
            model_name='atuacao',
            name='segmento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='graph.Segmento'),
        ),
    ]
