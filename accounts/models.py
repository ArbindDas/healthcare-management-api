


from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager


class Role(models.TextChoices):
    ADMIN = "ADMIN", "admin"
    DOCTOR = "DOCTOR", "doctor"
    PATIENT = "PATIENT", "patient"
    


class UserManager(BaseUserManager):
    def create_user(self , email , password=None, full_name=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        if not full_name:
            raise ValueError("Fullname is required")
        
        
        email = self.normalize_email(email)
        
        user = self.model(
            email = email,
            full_name=full_name,
            **extra_fields
        )
    
    
        user.set_password(password)
        user.save(using=self._db)
        
        
        return user
    
    
    def create_superuser(self , email, password=None , full_name=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        return self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            **extra_fields
        )
    
    
   
        
    

class User(AbstractUser):
        username = None
        email = models.EmailField(unique=True)
        full_name = models.CharField(max_length=150)
        
        
        
        role = models.CharField(
            max_length=20,
            choices=Role.choices,
            default= Role.PATIENT
        )

        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = ["full_name"]
        
        
        objects =  UserManager()
        
        
        def __str__(self):
            return self.email