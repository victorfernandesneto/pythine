# Generated by Django 4.2.7 on 2023-11-09 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 9, 12, 45, 54, 522950)),
        ),
    ]
