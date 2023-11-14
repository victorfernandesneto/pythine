from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index_view(request):
    if request.user.is_authenticated:
        return redirect('task_index')
    user = request.user
    print(user.username)
    return render(request, 'login/index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('task_index')
            else:
                form = LoginForm()
    else:
        form = LoginForm()
    return render(request,
                  'login/login.html',
                  {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('task_index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form['username'].value()
            senha = form['password1'].value()
            user = User.objects.create_user(username=usuario, password=senha)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(
        request,
        'login/register.html',
        {'form': form}
        )


def logout_view(request):
    logout(request)
    return redirect('index')