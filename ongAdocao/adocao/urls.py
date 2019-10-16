from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('listaAnimais/',views.listaAnimais,name='listaAnimais'),
    path('teste/<int:idAnimal>',views.teste,name='teste'),

]
