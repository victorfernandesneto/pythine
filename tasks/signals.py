from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, **kwargs):
    subject = 'New task in Pythine'
    deadline = instance.deadline.strftime("%d/%m/%Y %H:%M")
    message = f'You have to do something!!\n\nTask name: {instance.task_name}\nDeadline: {deadline}\n\nPythine'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [instance.user.email]
    send_mail(subject, message, from_email, recipient_list)