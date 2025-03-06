from django.shortcuts import render, redirect
from config.settings import MEDIA_ROOT
from .models import *
# Create your views here.
def index(request):
    titles = Category.title
    title = Product.title
    description = Product.description
    price = Product.price
    image = Product.image

    ctx = {
        'titles': titles,
        'title': title,
        'description': description,
        'price': price,
        'image': image,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'food/index.html', ctx)
    return response