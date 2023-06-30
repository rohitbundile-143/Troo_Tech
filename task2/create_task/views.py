

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .task import send_excel_email_task

@api_view(['POST'])
def send_excel_email(request):
    email = request.data.get('email')

    # Schedule the task using Celery's apply_async method
    send_excel_email_task.apply_async(args=[email])

    return Response({'message': 'Email scheduled successfully'})
