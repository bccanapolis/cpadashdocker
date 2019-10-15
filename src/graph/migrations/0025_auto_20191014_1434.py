# Generated by Django 2.2.6 on 2019-10-14 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0024_auto_20191014_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segmento',
            name='atuacao',
        ),
        migrations.RemoveField(
            model_name='segmento',
            name='lotacao',
        ),
        migrations.AddField(
            model_name='perguntasegmento',
            name='atuacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='graph.Atuacao'),
        ),
        migrations.AddField(
            model_name='perguntasegmento',
            name='lotacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='graph.Lotacao'),
        ),
    ]