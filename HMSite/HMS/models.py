from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Doctor(AbstractBaseUser):
    identifier = models.CharField(max_length=20, unique=True)
    USERNAME_FIELD = 'identifier'
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True,)
    is_active=models.BooleanField(default=True)
    is_content_manager=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    