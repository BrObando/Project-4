from django.shortcuts import render

from django.http import JsonResponse

from django.contrib.auth.models import User 

# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import DonorForm, BloodInventoryForm
from .models import Donor, BloodInventory

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
            donor = form.save()

            try:
                blood_inventory = BloodInventory.objects.get(blood_type=donor.blood_type)
                blood_inventory.units_available += donor.units_collected
                blood_inventory.save()
            except BloodInventory.DoesNotExist:
                
                pass

            return redirect('donor_list')
    else:
        form = DonorForm()

    return render(request, 'authentication/register_donor.html', {'form': form})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'authentication/donor_list.html', {'donors': donors})

def blood_inventory_list(request):
    inventories = BloodInventory.objects.all()
    return render(request, 'authentication/blood_inventory_list.html', {'inventories': inventories})

def create_blood_inventory(request):
    if request.method == 'POST':
        form = BloodInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood_inventory_list')
    else:
        form = BloodInventoryForm()

    return render(request, 'authentication/create_blood_inventory.html', {'form': form})

def update_blood_inventory(request, pk):
    inventory = get_object_or_404(BloodInventory, pk=pk)

    if request.method == 'POST':
        form = BloodInventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('blood_inventory_list')
    else:
        form = BloodInventoryForm(instance=inventory)

    return render(request, 'authentication/update_blood_inventory.html', {'form': form, 'inventory': inventory})



def delete_blood_inventory(request, pk):
    inventory = get_object_or_404(BloodInventory, pk=pk)
    inventory.delete()
    return redirect('blood_inventory_list')



from django.shortcuts import get_object_or_404

def ajax_blood_inventory(request):
    
    blood_inventory = BloodInventory.objects.get(pk=1)  

    
    data = {
        'units_available': blood_inventory.units_available,
        'threshold': blood_inventory.threshold,
    }

    
    if blood_inventory.units_available <= blood_inventory.threshold:
        data['notify'] = True
        data['message'] = 'Blood inventory is below the threshold!'

    return JsonResponse(data)




from .forms import BloodShipmentForm
from .models import BloodShipment, BloodInventory





def initiate_blood_shipment(request):
    if request.method == 'POST':
        form = BloodShipmentForm(request.POST)
        if form.is_valid():
            blood_shipment = form.save(commit=False)

            
            blood_inventory = BloodInventory.objects.filter(units_available__gte=blood_shipment.units_shipped).first()

            if blood_inventory:
                blood_shipment.blood_inventory = blood_inventory
                blood_shipment.sender = request.user  
                blood_shipment.save()

                
                blood_inventory.units_available -= blood_shipment.units_shipped
                blood_inventory.save()

                return redirect('blood_shipment_list')
            else:
                form.add_error(None, "No suitable blood inventory available for shipment.")
    else:
        form = BloodShipmentForm()

    return render(request, 'authentication/initiate_blood_shipment.html', {'form': form})


def blood_shipment_list(request):
    shipments = BloodShipment.objects.all()
    return render(request, 'authentication/blood_shipment_list.html', {'shipments': shipments})