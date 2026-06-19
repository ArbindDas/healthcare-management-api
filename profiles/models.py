from django.db import models
from django.conf import settings




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15 , blank=True, null=True)
    address = models.TextField(blank=True , null=True)
    
    
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.email
    
    
    
    
class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile"
    )
    specialization = models.CharField(max_length=150)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.user.full_name}"


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )
    blood_group = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.user.full_name}"


class Appointment(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    appointment_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ("PENDING", "Pending"),
            ("APPROVED", "Approved"),
            ("COMPLETED", "Completed"),
            ("CANCELLED", "Cancelled")
        ],
        default="PENDING"
    )

    def __str__(self):
        return f"{self.patient} -> {self.doctor} ({self.status})"
    
    
    
    
