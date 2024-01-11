from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    blood_type = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.blood_type}"