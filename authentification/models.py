from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBCRIBER = 'SUBCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Createur'),
        (SUBCRIBER, 'Abonne')
    )

    profile_phot0 = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)