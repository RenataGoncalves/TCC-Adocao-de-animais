from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('descricao/<int:idAnimal>',views.descricao,name='descricao'),
    path('ajuda', views.ajuda, name='ajuda'),

]
