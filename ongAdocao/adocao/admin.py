from django.contrib import admin
from .models import Pessoa, Animal, Adocao, Imagens
from django.utils.html import format_html

class ImagensAdmin(admin.ModelAdmin):      
    
    def image_tag(self, obj):
        return format_html('<img src="{}"  width="130" height="120" />'.format(obj.imagem.url))

    image_tag.short_description = 'Imagem'
    list_display = (['animal','image_tag'])
    search_fields = ['nome']
        

class ImagensInline(admin.StackedInline):
    model = Imagens
    extra = 1
   

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nome','especie','sexo','porte']
    #list_display = ['nomeAnimal','get_sexo_display', 'get_especie_display', 'get_porte_display','map_sexo', 'map_porte']
    search_fields = ['nome']
    inlines = [ImagensInline]       


class AdocaoAdmin(admin.ModelAdmin):
    list_display = ['animal','pessoa','funcionario','data_adocao']


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Pessoa)
admin.site.register(Adocao, AdocaoAdmin)
admin.site.register(Imagens, ImagensAdmin)

admin.site.site_header = "Administração da OngAdoção"
