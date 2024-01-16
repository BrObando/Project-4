from django.shortcuts import render
# from .forms import FutureDonorForm
from django.conf import settings 
from django.core.mail import send_mail



def home(request):
  
  return render(request, 'home.html')


# def future_donor(request):
#     if request.method == 'POST':
#         form = FutureDonorForm(request.POST)
#         if form.is_valid():
#             # Process form data

#             # Send confirmation email
#             subject = 'Appointment Confirmation'
#             message = 'Thank you for scheduling an appointment!'
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [form.cleaned_data['email']]
#             send_mail(subject, message, from_email, recipient_list)

#             return render(request, 'confirmation_page.html')
#     else:
#         form = FutureDonorForm()

#     return render(request, 'main_app/future_donor.html', {'form': form})


def future_donor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        # Retrieve other form fields as needed

        # Process form data

        # Send confirmation email
        subject = 'Appointment Confirmation'
        message = 'Thank you for scheduling an appointment!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'confirmation_page.html')

    return render(request, 'main_app/future_donor.html')