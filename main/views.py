from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from goods.models import Categories

def index(request):

    context = {
        'title': 'Yare Yare Daze',
        'content': "Доставка еды японской кухни",
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': "Доставка еды японской кухни"
    }
    return render(request, 'main/about.html', context)
