from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator 



class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    blood_type = models.CharField(max_length=5)
    units_collected = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.blood_type}"

class BloodInventory(models.Model):
    blood_type = models.CharField(max_length=5, unique=True)
    units_available = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.blood_type} - {self.units_available} units available"
    
    def add_units(self, units):
        self.units_available += units
        self.save()


from django.utils import timezone



class BloodShipment(models.Model):
    blood_inventory = models.ForeignKey(BloodInventory, on_delete=models.CASCADE)
    shipment_date = models.DateField()
    recipient = models.CharField(max_length=100)
    destination = models.CharField(max_length=255, default="Emergency Room")
    units_shipped = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    sender_name = models.CharField(max_length=255, default="Staff")

    def save(self, *args, **kwargs):
        
        if not self.sender and hasattr(self, 'request') and self.request.user.is_authenticated:
            self.sender = self.request.user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.units_shipped} units of {self.blood_inventory.blood_type} blood shipped on {self.shipment_date}"