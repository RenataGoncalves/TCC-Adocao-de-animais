from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from django.contrib.auth.models import User

class Animal(models.Model):
    imagemAnimal = models.ImageField(upload_to='images/')
    descricao = models.CharField(
        max_length=255, null=False, blank=False
    )
    nomeAnimal = models.CharField(
        max_length=255, null=False, blank=False
    )
    adotado = models.BooleanField(default=False)
    macho = 1
    femea = 2
    gato = 3
    cachorro = 4
    pequeno = 5
    medio = 6
    grande = 7
    naoInformado = 8
    escolhasS = (
        (1, 'Macho'),
        (2, 'Femea'),
        (8, 'Nao informado')
    )
    escolhasR = (
        (3, 'Gato'),
        (4, 'Cachorro'),
        (8, 'Nao informado')
    )
    escolhasP = (
        (5, 'Pequeno'),
        (6, 'Medio'),
        (7, 'Grande'),
        (8, 'Nao informado')
    )
    sexo = models.IntegerField(choices=escolhasS, default=8)
    especie = models.IntegerField(choices=escolhasR, default=8)
    porte = models.IntegerField(choices=escolhasP, default=8)

    def __str__(self):
        return f"{self.nomeAnimal} ({self.descricao})"

    class Meta:
        verbose_name_plural = 'animais'

class Pessoa(models.Model):
    nomePessoa = models.CharField(
        max_length=255, null=False, blank=False
    )
    telefonePessoa = models.CharField(
        max_length=30, null=False, blank=False
    )
    cpfPessoa = models.CharField(
        max_length=11, null=False, blank=False
    )
    enderecoPessoa= models.CharField(
        max_length=255, null=False, blank=False
    )

    def __str__(self):
        return self.nomePessoa


class Adocao(models.Model):
    data_adocao =  models.DateTimeField(default=now, editable=False)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.animal.nomeAnimal

    class Meta:
        verbose_name_plural = 'adoções'