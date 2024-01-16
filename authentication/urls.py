from django.urls import path
from .views import login_view, logout_view, change_password, dashboard, register_donor, donor_list, schedule_appointment, record_blood_donation

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register-donor/', register_donor, name='register_donor'),
    path('donor-list/', donor_list, name='donor_list'),
    path('schedule-appointment/', schedule_appointment, name='schedule_appointment'),
    path('record-blood-donation/', record_blood_donation, name='record_blood_donation'),
    path('record-blood-donation/<int:donation_id>/', record_blood_donation, name='record_blood_donation_with_id'),
]