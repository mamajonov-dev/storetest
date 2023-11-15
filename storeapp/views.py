from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import *
from .models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request, slug=None, page_number=1):
    if slug:
        category = CategoryModel.objects.get(slug=slug)
        product = ProductModel.objects.filter(category=category)
    else:
        product = ProductModel.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    products_paginator = paginator.page(page_number)
    data = {
        'categories': CategoryModel.objects.all(),
        'products': products_paginator,

    }
    return render(request, 'products.html', context=data)


def success(request):
    return render(request, 'orders/success.html')


def email_verification(request):
    return render(request, 'users/email_verification.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserLoginForm()
    data = {'form': form}
    return render(request, 'users/login.html', context=data)


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/login/')
def user_profile(request):
    if request.method == 'POST':
        form = UserProfile_Form(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            return print(form.errors)
    else:
        form = UserProfile_Form(instance=request.user)
    baskets = BasketModel.objects.filter(user=request.user)

    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        if basket.order == False:
            total_quantity = total_quantity + 1
            total_sum = total_sum + basket.sum()

    context = {
        'form': form,
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum
    }
    return render(request, 'users/profile.html', context)


@login_required(login_url='/login/')
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
    except:
        pass
    return redirect('home')


def userregistration(request):
    if request.method == 'POST':
        form = UserRegistrForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Muvaffaqqiyatli ro\'yxatdan o\'tdingiz!')
            return redirect('login')
    else:
        form = UserRegistrForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


def orders(request):

    orders = OrderModel.objects.filter(user=request.user)
    context = {
        'orders': orders
    }

    return render(request, 'orders/orders.html', context)


def order_page(request):
    baskets = BasketModel.objects.filter(user=request.user, order=False)
    for basket in baskets:
        orders = OrderModel.objects.filter(user=request.user, basket=basket)
        if not orders.exists():
            OrderModel.objects.create(user=request.user, basket=basket)
            basket.order = 'True'
            basket.save()

    context = {
        'orders': OrderModel.objects.filter(user=request.user)
    }
    return render(request, 'orders/order.html', context)


def order_careate(request):
    if request.method == 'POST':
        form = UserProfile_Form(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success'))
        else:
            return messages.error(request, messages.error)
    else:
        form = UserProfile_Form(instance=request.user)

    baskets = BasketModel.objects.filter(user=request.user, order=False)

    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum = total_sum + basket.sum()
        total_quantity += 1

    context = {
        'form': form,
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity
    }
    return render(request, 'orders/order-create.html', context)


@login_required(login_url='/login/')
def basket_add(request, product_id):
    product = ProductModel.objects.get(id=product_id)
    baskets = BasketModel.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        BasketModel.objects.create(user=request.user, product=product, quantity=1)
    else:
        for basket in baskets:
            if basket.order == False:
                basket = baskets.first()
                basket.quantity += 1
                basket.save()
            else:
                BasketModel.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def delete_basket(request, basket_id):
    basket = BasketModel.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
