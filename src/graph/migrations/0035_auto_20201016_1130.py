# Generated by Django 2.2 on 2020-10-16 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0034_auto_20201016_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participacaopergunta',
            old_name='created_at',
            new_name='ano',
        ),
    ]