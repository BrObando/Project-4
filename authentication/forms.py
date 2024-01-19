

from django import forms
from .models import Donor, BloodInventory
from django.core.validators import MinValueValidator 

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


class BloodInventoryForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'units_available']


from .models import BloodShipment


class BloodShipmentForm(forms.ModelForm):
    units_shipped = forms.IntegerField(
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Units Shipped'
    )

    blood_type = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Blood Type'
    )

    class Meta:
        model = BloodShipment
        fields = ['shipment_date', 'recipient', 'destination', 'units_shipped', 'blood_type']
