# Generated by Django 2.2.6 on 2019-10-08 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0020_remove_pessoa_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoacurso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.CursoCampus'),
        ),
    ]
