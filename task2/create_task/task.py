# emailapp/tasks.py

import pandas as pd
from celery import shared_task
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

@shared_task
def send_excel_email_task(email):
    users = User.objects.all()

    # Create DataFrame from user data
    data = {
        'id': [user.id for user in users],
        'name': [user.username for user in users],
        'is_active': [user.is_active for user in users],
    }
    df = pd.DataFrame(data)

    # Create Excel file
    excel_file = 'users.xlsx'
    df.to_excel(excel_file, index=False)

    # Send email with Excel file as an attachment
    subject = 'User Data'
    body = 'Please find the attached Excel file containing user data.'
    from_email = 'your@email.com'
    to_email = [email]

    email_message = EmailMessage(subject, body, from_email, to_email)
    email_message.attach_file(excel_file)
    email_message.send()

    return 'Email sent successfully'
