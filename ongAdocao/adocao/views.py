from django.shortcuts import render
from .models import Animal
from django.core.paginator import Paginator





def teste(request,idAnimal):
    animal = Animal.objects.get(id=idAnimal)
    return render(request, 'descricao.html',{'animal':animal})


def index(request):
	animais = Animal.objects.filter(adotado=False)
	adotados = Animal.objects.filter(adotado=True)[:4]
	paginator = Paginator(animais, 8)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'index.html',{'animais':posts,'animaisAdotados':adotados})





