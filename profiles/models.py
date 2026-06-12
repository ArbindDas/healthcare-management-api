from django.db import models
from django.conf import settings


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
    
    
    
    
class Test(models.Model):
    username = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return f"{self.username}"