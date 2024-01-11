from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import DonorForm
from .models import Donor

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid login credentials.'
            return render(request, 'authentication/login.html', {'error_message': error_message})
    return render(request, 'authentication/login.html', {'user': None})

def logout_view(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html', {'form': form})

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'authentication/register_donor.html', {'form': form})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'authentication/donor_list.html', {'donors': donors})