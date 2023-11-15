from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['task_name', 'deadline', 'description']
        labels = {
            'task_name': 'Task name',
            'deadline': 'DEADLINE',
            'description': 'Description'
        }
        widgets = {
            'task_name': forms.TextInput(),
            'deadline': forms.DateTimeInput(format='%d/%m/%Y %H:%M',
                                            attrs={'type': 'datetime-local'}),
            'description': forms.TextInput()
        }
