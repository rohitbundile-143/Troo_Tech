# emailapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta
from .tasks import send_email_task
from .serializers import ScheduledEmailSerializer
from django.utils import timezone

@api_view(['POST'])
def schedule_email(request):
    serializer = ScheduledEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']

        # Calculate the scheduled time for sending the email
        scheduled_time = timezone.now() + timedelta(minutes=2)

        # Schedule the task using Celery's apply_async method
        send_email_task.apply_async(args=[email], eta=scheduled_time)

        return Response({'message': 'Email scheduled successfully'})
    else:
        return Response(serializer.errors, status=400)
