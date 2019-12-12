from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from django.contrib.auth.models import User


class Animal(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    historia = models.TextField(null=False, blank=False)
    adotado = models.BooleanField(default=False)
    data =  models.DateTimeField(default=now, editable=False)
    macho = 1
    femea = 2
    gato = 3
    cachorro = 4
    pequeno = 5
    medio = 6
    grande = 7
    nao_informado = 8
    
    escolhasS = (
        (macho, 'Macho'),
        (femea, 'Femea'),
        (nao_informado, 'Nao informado')
    )
    escolhasR = (
        (gato, 'Gato'),
        (cachorro, 'Cachorro'),
        (nao_informado, 'Nao informado')
    )
    escolhasP = (
        (pequeno, 'Pequeno'),
        (medio, 'Médio'),
        (grande, 'Grande'),
        (nao_informado, 'Nao informado')
    )
    

    sexo = models.IntegerField(choices=escolhasS, default=8)
    especie = models.IntegerField(choices=escolhasR, default=8)
    porte = models.IntegerField(choices=escolhasP, default=8)
   

    def __str__(self):
        return f"{self.nome} ({self.descricao})"
    
    class Meta:
        ordering = ['-data']

class Pessoa(models.Model):
    nome = models.CharField(
        max_length=255, null=False, blank=False
    )
    telefone = models.CharField(
        max_length=30, null=False, blank=False
    )
    cpf = models.CharField(
        max_length=11, null=False, blank=False
    )
    endereco = models.CharField(
        max_length=255, null=False, blank=False
    )

    def __str__(self):
        return self.nome

class Adocao(models.Model):
    data_adocao =  models.DateTimeField(default=now, editable=False)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.animal.nome

    class Meta:
        verbose_name_plural = 'adoções'


class Imagens(models.Model):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE, related_name = "imagens")
    #animal.imagens 
    imagem = models.ImageField(null=True, upload_to='images/')

    class Meta:
        verbose_name_plural = 'Imagens'


























