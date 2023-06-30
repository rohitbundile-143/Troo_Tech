# tasks.py

# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(email):
    subject = 'Email Subject'
    message = 'Email Message'
    from_email = 'your@email.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
