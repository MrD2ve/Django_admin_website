from django.shortcuts import render, redirect
from config.settings import MEDIA_ROOT
from .models import *
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price", 0)
    print(orders_list)
    print(total_price)

    ctx = {
        'categories': categories,
        'products': products,
        'orders': orders,
        'total_price': total_price,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'food/index.html', ctx)
    response.set_cookie("greeting", 'hello')
    return response