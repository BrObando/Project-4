from django.urls import path
from .views import login_view, logout_view, change_password, dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('dashboard/', dashboard, name='dashboard'),
]