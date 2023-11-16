from django.urls import path
from .views import TaskListView, CreateTaskView, TaskDeleteView, TaskUpdateView


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('add/', CreateTaskView.as_view(), name='new_task'),
    path('delete_task/<int:id>', TaskDeleteView.as_view(), name='delete_task'),
    path('task_update/<int:id>', TaskUpdateView.as_view(), name='task_update')    
]
