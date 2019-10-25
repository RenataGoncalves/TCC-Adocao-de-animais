from django.contrib import admin
from .models import Pessoa, Animal, Adocao, Imagens

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nomeAnimal','sexo', 'especie']
    #list_display = ['nomeAnimal','get_sexo_display', 'get_especie_display', 'get_porte_display','map_sexo', 'map_porte']
    search_fields = ['imagem_animal','nomeAnimal']

admin.site.register(Pessoa)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Adocao)
admin.site.register(Imagens)


admin.site.site_header = "Administração da OngAdoção"
