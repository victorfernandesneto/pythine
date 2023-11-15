from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('add/', CreateTaskView.as_view(), name='new_task'),
    path('delete_task/<id>', TaskDeleteView.as_view(), name='delete_task'),
    path('toggle_task/<id>', toggle_finish_task_view, name='toggle_finish_task')    
]
