from django.urls import path 
from . import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('future_donor/', views.future_donor, name='future_donor'),
]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/', include('authentication.urls')),
# ]