from django.urls import path
from emergency import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drive', views.drive, name='drive'),
    path('staff', views.staff, name='staff'),
    path('car_list', views.car_list, name='car_list'),
]
