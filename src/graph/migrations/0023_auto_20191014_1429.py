# Generated by Django 2.2.6 on 2019-10-14 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0022_lotacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atuacao',
            name='segmento',
        ),
        migrations.RemoveField(
            model_name='lotacao',
            name='segmento',
        ),
        migrations.AddField(
            model_name='pergunta',
            name='atuacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='graph.Atuacao'),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='lotacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='graph.Lotacao'),
        ),
    ]
