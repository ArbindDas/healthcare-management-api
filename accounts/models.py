from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
# Create your models here.
class Role(models.TextChoices):
    ADMIN="ADMIN"
    DOCTOR="DOCTOR"
    PATIENT="PATIENT"
    
    


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, full_name=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, full_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, full_name, **extra_fields)
    
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
   
    objects = UserManager()   # 🔥 THIS LINE IS MISSING IN YOUR CODE
   
