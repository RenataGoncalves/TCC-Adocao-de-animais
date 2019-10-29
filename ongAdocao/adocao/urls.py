from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teste/<int:idAnimal>',views.teste,name='teste'),

]
