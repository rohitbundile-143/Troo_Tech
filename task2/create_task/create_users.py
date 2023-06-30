# create_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create 100 users in the system'

    def handle(self, *args, **options):
        for i in range(1, 101):
            username = f'user{i}'
            password = f'password{i}'
            User.objects.create_user(username=username, password=password)

            self.stdout.write(self.style.SUCCESS(f'User {username} created successfully'))
