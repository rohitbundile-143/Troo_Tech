# emailapp/models.py

from django.db import models

class ScheduledEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
