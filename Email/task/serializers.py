# emailapp/serializers.py

from rest_framework import serializers
from .models import ScheduledEmail

class ScheduledEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEmail
        fields = ('email',)
