from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Category, Customer, Product, Order
from .forms import SignUpForm

#Product by category
def category(request, cat):
    #Replace Hyphens with spaces
    cat = cat.replace('-',' ')
    #Grab the category from the url
    try:
        #Look up the category
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request,'store/category.html', {
            'products': products,
            'category': category
        })
    except:
        messages.success(request, ("Category doesnt exist"))
        return redirect('home')


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

#About View
def about(request):
    return render(request, "store/about.html", {})

#Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Error. You should check in on some of those fields below."))
            return redirect('login')
    else:
        return render(request, 'store/login.html', {})

#Logout
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logout."))
    return redirect('home')

def register_user(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully! "))
            return redirect('home')
        else:
            messages.success(request, ("Please Try again."))
            return redirect('register')

    else:
        return render(request, 'store/register.html', {'form':form})