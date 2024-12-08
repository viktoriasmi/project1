from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import context

from goods.models import Categories
from main.models import News

def index(request):
    latest_news = News.objects.order_by('-publication_date').first()
    context = {
        'title': 'Yare Yare Daze',
        'latest_news': latest_news,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': "Доставка еды японской кухни"
    }
    return render(request, 'main/about.html', context)

def news(request):
    news_items = News.objects.all()
    context = {
        'title': 'Новости',
        'news_items': news_items,
    }
    return render(request, 'main/news.html', context)

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    context = {
        'title': 'Новость',
        'news_item': news_item,
    }
    return render(request, 'main/news_detail.html', context)

def delivery(request):
    context = {
        'title': 'Информация о доставке',
    }
    return render(request, 'main/delivery.html', context)
