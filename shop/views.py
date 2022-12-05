from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from shop.models import Item


# Create your views here.

def index(request):
    return HttpResponse('Добро пожаловать в наш магазин')


def list_item(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'list_item.html', context)


def detail_item(request, id):
    items = get_object_or_404(Item, id=id)
    context = {
        'items': items,
    }
    return render(request, 'detail_item.html', context)
