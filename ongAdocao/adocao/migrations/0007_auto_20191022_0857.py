# Generated by Django 2.2 on 2019-10-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0006_auto_20191022_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='porte',
            field=models.CharField(choices=[(5, 'Pequeno'), (6, 'Médio'), (7, 'Grande'), (8, 'Nao informado')], default=8, max_length=8),
        ),
    ]
