# Generated by Django 2.2 on 2019-11-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagens',
            name='imagem_anima1',
        ),
        migrations.RemoveField(
            model_name='imagens',
            name='imagem_anima2',
        ),
        migrations.RemoveField(
            model_name='imagens',
            name='imagem_anima3',
        ),
        migrations.AlterField(
            model_name='imagens',
            name='imagem_animal',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
