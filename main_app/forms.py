
from django import forms

class FutureDonorForm(forms.Form):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    
