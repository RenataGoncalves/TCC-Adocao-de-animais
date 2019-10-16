# Generated by Django 2.2 on 2019-04-28 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagemAnimal', models.ImageField(upload_to='images/')),
                ('descricao', models.CharField(max_length=255)),
                ('nomeAnimal', models.CharField(max_length=255)),
                ('sexo', models.IntegerField(choices=[(1, 'Macho'), (2, 'Femea'), (8, 'Nao informado')], default=8)),
                ('raca', models.IntegerField(choices=[(3, 'Gato'), (4, 'Cachorro'), (8, 'Nao informado')], default=8)),
                ('porte', models.IntegerField(choices=[(5, 'Pequeno'), (6, 'Medio'), (7, 'Grande'), (8, 'Nao informado')], default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePessoa', models.CharField(max_length=255)),
                ('telefonePessoa', models.CharField(max_length=30)),
                ('cpfPessoa', models.CharField(max_length=11)),
                ('enderecoPessoa', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_adocao', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Animal')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Pessoa')),
            ],
        ),
    ]