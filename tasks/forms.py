from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'deadline']

    def save(self, request):
        task = Task(
            task_name=self.cleaned_data['task_name'],
            deadline=self.cleaned_data['deadline'],
            user=request.user
        )
        task.save()
        return task
    