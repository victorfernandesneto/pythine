from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(
        max_length=200,
        blank=False,
        null=False
    )
    deadline = models.DateTimeField(default=datetime.today(), blank=False)
    description = models.TextField(
        blank=True,
        null=False,
        default=''
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.task_name
    