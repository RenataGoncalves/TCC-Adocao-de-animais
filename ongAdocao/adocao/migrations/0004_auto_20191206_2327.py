# Generated by Django 2.2 on 2019-12-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0003_auto_20191102_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='castrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='animal',
            name='vacinado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='animal',
            name='vermifugado',
            field=models.BooleanField(default=False),
        ),
    ]
