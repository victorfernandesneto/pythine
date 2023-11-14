from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', task_index_view, name='task_index'),
    path('add/', new_task_view, name='new_task'),
    path('change/', toggle_finish_task, name='toggle_task'),
    path('delete_task/<id>', delete_task, name='delete_task'),
    
]
