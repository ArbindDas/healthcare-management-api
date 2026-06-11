from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Role(models.TextChoices):
    ADMIN="ADMIN"
    DOCTOR="DOCTOR"
    PATIENT="PATIENT"
    
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    full_name =  models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]
   