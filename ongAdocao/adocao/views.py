from django.shortcuts import render
from .models import Animal, Imagens
from django.core.paginator import Paginator

def descricao(request,idAnimal):
	contexto = {}
	animal = Animal.objects.get(id=idAnimal)
	imagens = Imagens.objects.filter(animal=animal)[1:]
	imagem1 = Imagens.objects.filter(animal=animal)[0]
	contexto['animal'] = animal
	contexto['imagens'] = imagens
	contexto['imagem1'] = imagem1

	return render(request, 'descricao.html',contexto)

def index(request):
	imagens = Imagens.objects.all()
	animais = Animal.objects.filter(adotado=False)
	adotados = Animal.objects.filter(adotado=True)[:4]
	paginator = Paginator(animais, 8)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'index.html',{'animais':posts,'animaisAdotados':adotados, 'imagens':imagens})