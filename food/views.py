from django.shortcuts import render, redirect
from config.settings import MEDIA_ROOT
from .models import *
from forms import *

import json
# Create your views here.


def index(request):
    titles = Category.objects.all()
    products = Product.objects.all()
    orders = []
    order_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price", 0)

    if order_list:
        for key, value in json.loads(order_list).item():
            orders.append(
                {
                    "product": Product.objects.get(pk=int(key)),
                    "count": value
                }
            )


    ctx = {
        'titles': titles,
        'products': products,
        'orders': orders,
        'total_price': total_price,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'food/index.html', ctx)
    return response