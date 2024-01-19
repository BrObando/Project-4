from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def home(request):

  return render(request, 'home.html')



def future_donor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        
        messages.success(request, 'Your appointment request was received successfully!')

        return render(request, 'main_app/confirmation_page.html')

    return render(request, 'main_app/future_donor.html')

