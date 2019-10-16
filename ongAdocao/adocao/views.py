from django.shortcuts import render
from .models import Animal
from django.core.paginator import Paginator



def listaAnimais(request):
    listaAnimais = Animal.objects.filter(adotado=False)
    return render(request, 'listaAnimais.html',{'animais':listaAnimais})

def teste(request,idAnimal):
    animal = Animal.objects.get(id=idAnimal)
    return render(request, 'descricao.html',{'animal':animal})


def index(request):
	index = Animal.objects.all()
	paginator = Paginator(index, 8)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'index.html', {'animais':posts})





