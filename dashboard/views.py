from django.shortcuts import render,redirect
from food.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    categorys = services.get_categories()
    products = services.get_products()
    users = services.get_users()
    orders = services.get_orders()
    ctx={
        'counts' : {
            'categorys':len(categorys),
            'products':len(products),
            'users':len(users),
            'orders':len(orders),
        }
    }
    return render(request, 'dashboard/index.html', ctx)

@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created category: {request.POST.get('name')}"]
        request.session["actions"] = actions

        category_count = request.session.get('category_count', 0)
        category_count += 1
        request.session["category_count"] = category_count
        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You edited category: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('category_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')

@login_required_decorator
def category_list(request):
    categories=services.get_categories()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'category/list.html',ctx)

# Product
@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created product: {request.POST.get('name')}"]
        request.session["actions"] = actions

        product_count = request.session.get('product_count', 0)
        product_count +=1
        request.session["product_count"] = product_count

        return redirect('product_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_edit(request,pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited product: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('product_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_delete(request,pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')

@login_required_decorator
def product_list(request):
    products=services.get_product()
    ctx={
        "products":products
    }
    return render(request,'product/list.html',ctx)

#Customer
@login_required_decorator
def customer_create(request):
    model = Customer()
    form = CustomerForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created customer: {request.POST.get('name')}"]
        request.session["actions"] = actions

        customer_count = request.session.get('customer_count', 0)
        customer_count += 1
        request.session["customer_count"] = customer_count
        return redirect('customer_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'customer/form.html',ctx)

@login_required_decorator
def customer_edit(request,pk):
    model = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You edited customer: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('customer_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'customer/form.html',ctx)

@login_required_decorator
def customer_delete(request,pk):
    model = Customer.objects.get(pk=pk)
    model.delete()
    return redirect('customer_list')

@login_required_decorator
def customer_list(request):
    customers=services.get_customer()
    ctx={
        "customers":customers
    }
    return render(request,'customer/list.html',ctx)

#Order
@login_required_decorator
def order_create(request):
    model = Order()
    form = OrderForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You created order: {request.POST.get('name')}"]
        request.session["actions"] = actions

        order_count = request.session.get('order_count', 0)
        order_count += 1
        request.session["order_count"] = order_count
        return redirect('order_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'order/form.html',ctx)

@login_required_decorator
def order_edit(request,pk):
    model = Order.objects.get(pk=pk)
    form = OrderForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You edited order: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('order_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'order/form.html',ctx)

@login_required_decorator
def order_delete(request,pk):
    model = Order.objects.get(pk=pk)
    model.delete()
    return redirect('order_list')

@login_required_decorator
def order_list(request):
    orders=services.get_order()
    ctx={
        "orders":orders
    }
    return render(request,'order/list.html',ctx)

@login_required_decorator
def profile(request):
    return render(request,'profile.html')