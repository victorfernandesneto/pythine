# Generated by Django 4.2.7 on 2023-11-15 17:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_alter_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='finished',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 15, 14, 17, 3, 658786)),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
