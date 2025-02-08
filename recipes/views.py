from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
    'name': 'Luiz Otávio viws',
})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
    })


def sobre(request):
    return HttpResponse('sobre')