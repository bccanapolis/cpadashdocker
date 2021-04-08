# Generated by Django 2.2 on 2021-03-20 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_auto_20210319_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursocampus',
            name='quant',
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='questionario',
        ),
        migrations.AddField(
            model_name='eixo',
            name='questionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='graph.Questionario'),
        ),
    ]