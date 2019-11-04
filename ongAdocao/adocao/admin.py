from django.contrib import admin
from .models import Pessoa, Animal, Adocao, Imagens

class ImagensAdmin(admin.ModelAdmin):
   list_display = [('animal')]
  

class ImagensInline(admin.StackedInline):
    model = Imagens
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    inlines = [
        ImagensInline
        ] 

# class AnimalAdmin(admin.ModelAdmin):
#     list_display = ['nome_animal','sexo', 'especie', 'porte']
#     #list_display = ['nomeAnimal','get_sexo_display', 'get_especie_display', 'get_porte_display','map_sexo', 'map_porte']
#     search_fields = ['nome_animal']

class AdocaoAdmin(admin.ModelAdmin):
    list_display = ['animal','pessoa','funcionario','data_adocao']


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Pessoa)
admin.site.register(Adocao, AdocaoAdmin)
admin.site.register(Imagens, ImagensAdmin)

admin.site.site_header = "Administração da OngAdoção"
