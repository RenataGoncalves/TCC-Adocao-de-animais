from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from django.contrib.auth.models import User

class Animal(models.Model):
    #imagemAnimal = models.ImageField(upload_to='images/')
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
    sexo = models.CharField(max_length=6, choices=escolhasS, default=8)
    especie = models.CharField(max_length=9, choices=escolhasR, default=8)
    porte = models.CharField(max_length=8, choices=escolhasP, default=8)

    def map_sexo(self):
        if self.sexo == self.macho:
            return "Macho"
        elif self.sexo == self.femea:
            return "Fêmea"
        elif self.sexo == self.nao_informado:
            return "Não informado"

    def map_porte(self):
        if self.porte == self.pequeno:
            return "Pequeno"
        elif self.porte == self.medio:
            return "Médio"
        elif self.porte == self.grande:
            return "Grande"
        elif self.porte == self.nao_informado:
            return "Não informado"

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

class Imagens(models.Model):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE, related_name = "imagens")
    #animal.imagens 
    imagem_animal = models.ImageField(upload_to='images/')
