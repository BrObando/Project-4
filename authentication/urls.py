from django.urls import path
from .views import login_view, logout_view, change_password, dashboard, register_donor, donor_list
from .views import blood_inventory_list, create_blood_inventory, update_blood_inventory, delete_blood_inventory
from .views import ajax_blood_inventory
from .views import initiate_blood_shipment, blood_shipment_list

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register-donor/', register_donor, name='register_donor'),
    path('donor-list/', donor_list, name='donor_list'),
    path('blood-inventory/', blood_inventory_list, name='blood_inventory_list'),
    path('blood-inventory/create/', create_blood_inventory, name='create_blood_inventory'),
    path('blood-inventory/update/<int:pk>/', update_blood_inventory, name='update_blood_inventory'),
    path('blood-inventory/delete/<int:pk>/', delete_blood_inventory, name='delete_blood_inventory'),
    path('auth/blood-inventory/', ajax_blood_inventory, name='ajax_blood_inventory'),
    path('initiate-blood-shipment/', initiate_blood_shipment, name='initiate_blood_shipment'),
    path('blood-shipment-list/', blood_shipment_list, name='blood_shipment_list'),

]