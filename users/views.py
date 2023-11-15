from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import FormView


class IndexView(TemplateView):
    template_name = 'login/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        return super().get(request)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login/login.html'
    success_url = '/tasks/'


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        return super().get(request)
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        return super().post(request)
    

    def form_valid(self, form):
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(self, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class CreateUserView(FormView):
    form_class = RegisterForm
    template_name = 'login/register.html'
    success_url = '/login/'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        return super().get(request)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('task_list')
        return super().post(request)

    def form_valid(self, form):
        username = form['username'].value()
        password = form['password1'].value()
        User.objects.create_user(username=username, password=password)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('index')
