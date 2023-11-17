from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['task_name', 'deadline',]
        labels = {
            'task_name': 'Task name',
            'deadline': 'DEADLINE',
        }
        widgets = {
            'task_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'deadline': forms.DateTimeInput(format='%d/%m/%Y %H:%M',
                                            attrs={'type': 'datetime-local',
                                                   'class': 'form-control mb-3'}),
        }
