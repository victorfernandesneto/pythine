from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, ListView, CreateView
from django.urls import reverse_lazy

def auth_user(request):
    if not request.user.is_authenticated:
            return True
    return False


class TaskListView(LoginRequiredMixin, ListView):
    login_url = 'index'
    redirect_field_name = ''
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self, **kwargs):
       user_id = self.request.user.id
       queryset = super().get_queryset(**kwargs)
       return queryset.filter(user_id=user_id)


class CreateTaskView(LoginRequiredMixin, CreateView):
    login_url = 'index'
    redirect_field_name = ''
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add.html'

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy('task_list')


def toggle_finish_task_view(request, id):
    # Conversar com o front end pra finalizado/não finalizado.
    pass


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'index'
    redirect_field_name = ''
    model = Task
    success_url = reverse_lazy('task_list')

    # Sobrescrever é necessário pra "pular" o template de confirmação.
    def get(self, request, *args, **kwargs): # Obs: não parece ser boa prática.
        return self.delete(request, *args, **kwargs)