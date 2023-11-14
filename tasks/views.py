from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_index_view(request):
    user_id = request.user.id
    tasks = Task.objects.filter(user_id=user_id)

    return render(
        request,
        'tasks/tasks.html',
        {'tasks': tasks}
    )


def new_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('task_index')
    else:
        form = TaskForm()
    return render(
        request,
        'tasks/add.html',
        {'form': form}
    )


def toggle_finish_task(request):
    # Conversar com o front end pra finalizado/não finalizado.
    return redirect('task_index')


def delete_task(request, id):
    query = Task.objects.get(id=id)
    # Fazer popup de "tem certeza?"
    query.delete()
    return redirect('task_index')
