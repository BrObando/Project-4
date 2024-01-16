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

class BloodDonation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_date = models.DateField()
    blood_type_collected = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.donor.username} - {self.donation_date}"


# from django.db import models
# from django.contrib.auth.models import User

# class Donor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     blood_type = models.CharField(max_length=5)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name} - {self.blood_type}"

# class BloodDonation(models.Model):
#     donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
#     donation_date = models.DateField()
#     blood_type_collected = models.CharField(max_length=5)

#     def __str__(self):
#         return f"{self.donor.user.username} - {self.donation_date}"