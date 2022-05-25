from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegistrationForm, UserAuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = UserRegistrationForm()
    return render(request, 'aligum/register.html', {'register_form': form})

def login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('index')
    else:
        form = UserAuthenticationForm
    return render(request, 'aligum/login.html', {'login_form':form})

def logout(request):
    logout(request)
    return redirect('login')

def gallery(request):
    images =Image.objects.all()
    return render(
        request,
        'aligum/gallery.html',
        {'images' : images}
    )

def index(request):
    products = Product.objects.all()
    return render(
        request,
        'aligum/index.html',
        {'products' : products}
    )

def about(request):
    return render(
        request,
        'aligum/about.html'
    )

def contact(request):
    return render(
        request,
        'aligum/contact.html'
    )
