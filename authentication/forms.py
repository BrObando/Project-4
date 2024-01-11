from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    BLOOD_TYPE_CHOICES = [
        ('SELECT ONE', 'SELECT ONE'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    blood_type = forms.TypedChoiceField(
        choices=BLOOD_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'blood_type']