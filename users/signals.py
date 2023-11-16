from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        subject = 'New member in Pythine'
        message = f'A new user joined us!!\n\nUsername: {instance.username}\nEmail: {instance.email}\n\nPythine'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_GOD]
        send_mail(subject, message, from_email, recipient_list)