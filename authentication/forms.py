from django import forms
from .models import Donor, BloodDonation
from django.contrib.auth.models import User

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

class BloodDonationForm(forms.ModelForm):
    class Meta:
        model = BloodDonation
        fields = ['donor', 'donation_date', 'blood_type_collected']

    def __init__(self, *args, **kwargs):
        user_queryset = kwargs.pop('user_queryset', None)
        super(BloodDonationForm, self).__init__(*args, **kwargs)
        if user_queryset:
            self.fields['donor'].queryset = user_queryset
            self.fields['donor'].widget = forms.Select(choices=[(user.id, user.username) for user in user_queryset])

