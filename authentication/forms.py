# from django import forms
# from .models import Donor
# from django.contrib.auth.models import User

# class DonorForm(forms.ModelForm):
#     BLOOD_TYPE_CHOICES = [
#         ('SELECT ONE', 'SELECT ONE'),
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     ]

#     blood_type = forms.TypedChoiceField(
#         choices=BLOOD_TYPE_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#     )

#     class Meta:
#         model = Donor
#         fields = ['first_name', 'last_name', 'contact_number', 'email', 'blood_type']

# class BloodDonationForm(forms.ModelForm):
#     class Meta:
#         model = BloodDonation
#         fields = ['donor', 'donation_date', 'blood_type_collected']

#     def __init__(self, *args, **kwargs):
#         user_queryset = kwargs.pop('user_queryset', None)
#         super(BloodDonationForm, self).__init__(*args, **kwargs)
#         if user_queryset:
#             self.fields['donor'].queryset = user_queryset
#             self.fields['donor'].widget = forms.Select(choices=[(user.id, user.username) for user in user_queryset])

# class BloodDonationForm(forms.ModelForm):
#     class Meta:
#         model = BloodDonation
#         fields = ['donor', 'donation_date', 'blood_type_collected']

#     def __init__(self, *args, **kwargs):
#         user_queryset = kwargs.pop('user_queryset', None)
#         super(BloodDonationForm, self).__init__(*args, **kwargs)
#         if user_queryset:
#             self.fields['donor'].queryset = user_queryset
#             self.fields['donor'].widget = forms.Select(choices=[(user.id, user.username) for user in user_queryset])


# from django import forms
# from .models import Donor

# class DonorForm(forms.ModelForm):
#     BLOOD_TYPE_CHOICES = [
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     ]

#     blood_type = forms.TypedChoiceField(
#         choices=BLOOD_TYPE_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#     )

#     units_collected = forms.IntegerField(
#         label='Units Collected',
#         widget=forms.NumberInput(attrs={'class': 'form-control'}),
#         min_value=0,
#     )

#     class Meta:
#         model = Donor
#         fields = ['first_name', 'last_name', 'contact_number', 'email', 'blood_type', 'units_collected']

from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):


    blood_type = forms.CharField(
        label='Blood Type',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=3,  
    )

    units_collected = forms.IntegerField(
        label='Units Collected',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0,
    )

    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'blood_type', 'units_collected']
