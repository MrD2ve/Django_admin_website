from django.shortcuts import render,redirect
from food.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

def login_page(request):
    if request.POST:
        username =request.POST.get("username",None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request,'dashboard/login.html')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required_decorator
def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    categories_products = []
    table_list = services.get_table()
    for category in categories:
        categories_products.append(
            {
                "category": category.title,
                "product": len(Product.objects.filter(category_id=category.id))
            }
        )
    ctx={
        'counts' : {
            'categories':len(categories),
            'products':len(products),
            'users':len(customers),
            'orders':len(orders),
        },
        "categories_products": categories_products,
        "tabel_list": table_list
    }
    return render(request, 'dashboard/index.html', ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created category: {request.POST.get('title')}"]
        request.session["actions"] = actions

        category_count = request.session.get('category_count', 0)
        category_count += 1
        request.session["category_count"] = category_count
        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'dashboard/category/form.html',ctx)

@login_required_decorator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You edited category: {request.POST.get('title')}"]
        request.session["actions"] = actions
        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'dashboard/category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')

@login_required_decorator
def category_list(request):
    categories=Category.objects.all()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'dashboard/category/list.html',ctx)

# Product
@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created product: {request.POST.get('title')}"]
        request.session["actions"] = actions

        product_count = request.session.get('product_count', 0)
        product_count += 1
        request.session["product_count"] = product_count
        return redirect('product_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def product_edit(request,pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/product/form.html', ctx)

@login_required_decorator
def product_delete(request,pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')

@login_required_decorator
def product_list(request):
    products=Product.objects.all()
    ctx={
        "product":products
    }
    return render(request,'dashboard/product/list.html',ctx)
#Customer

@login_required_decorator
def customer_create(request):
    model = Customer()
    form = CustomerForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('customer_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/customer/form.html',ctx)

@login_required_decorator
def customer_edit(request, pk):
    model = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('customer_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/customer/form.html',ctx)


@login_required_decorator
def customer_delete(request,pk):
    model = Customer.objects.get(pk=pk)
    model.delete()
    return redirect('customer_list')

@login_required_decorator
def customer_list(request):
    customers=Customer.objects.all()
    ctx={
        "customer":customers
    }
    return render(request,'dashboard/customer/list.html',ctx)

#Order
@login_required_decorator
def order_delete(request,pk):
    model = Order.objects.get(pk=pk)
    model.delete()
    return redirect('order_list')

@login_required_decorator
def order_list(request):
    orders=Order.objects.all()
    ctx={
        "orders":orders
    }
    return render(request,'dashboard/order/list.html',ctx)

@login_required_decorator
def profile(request):
    return render(request,'dashboard/profile.html')

@login_required_decorator
def customer_order_list(request,id):
    customer_orders = services.get_order_by_user(id=id)
    ctx = {
        'customer_orders': customer_orders
    }
    return render(request, "dashboard/customer_order/list.html", ctx)

@login_required_decorator
def orderproduct_list(request,id):
    productorders = services.get_product_by_order(id=id)
    ctx = {
        'productorders': productorders
    }
    return render(request, "dashboard/productorder/list.html", ctx)