# Generated by Django 2.2.6 on 2019-10-07 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0013_pergunta_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerguntaSegmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.Segmento')),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.Pergunta')),
            ],
            options={
                'verbose_name_plural': 'PerguntaSegmento',
            },
        ),
    ]
