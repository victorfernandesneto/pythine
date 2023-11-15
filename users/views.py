from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView


def auth_user(request):
    if request.user.is_authenticated:
            return True
    return False


class IndexView(View):

    def get(self, request):
        if auth_user(request):
            return redirect('task_list')
        return render(request, 'login/index.html')


class LoginView(View):
   
    def get(self, request):
        if auth_user(request):
            return redirect('task_list')
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})
    

    def post(self, request):
        if auth_user(request):
            return redirect('task_list')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')


class RegisterView(View):

    def get(self, request):
        if auth_user(request):
            return redirect('task_list')
        form = RegisterForm()
        return render(request, 'login/register.html', {'form': form})
    

    def post(self, request):
        if auth_user(request):
            return redirect('task_list')
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form['username'].value()
            senha = form['password1'].value()
            user = User.objects.create_user(username=usuario, password=senha)
            user.save()
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('index')
