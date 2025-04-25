from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    experience = models.PositiveIntegerField(help_text="Experience in years")

    def __str__(self):
        return self.name
    
class Doctor_info(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    specialty = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    hospital = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    payment_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name
