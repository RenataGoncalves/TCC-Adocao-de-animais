from django.shortcuts import render
from .models import Animal, Imagens
from django.core.paginator import Paginator

def descricao(request,idAnimal):
    animal = Animal.objects.get(id=idAnimal)
    return render(request, 'descricao.html',{'animal':animal})


def index(request):
	imagens = Imagens.objects.all()
	animais = Animal.objects.filter(adotado=False)
	adotados = Animal.objects.filter(adotado=True)[:4]
	paginator = Paginator(animais, 8)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'index.html',{'animais':posts,'animaisAdotados':adotados, 'imagens':imagens})