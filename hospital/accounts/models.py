from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES: tuple = (
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    )
    role: models.CharField = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self) -> str:
        return self.username