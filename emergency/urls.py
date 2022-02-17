from django.urls import path
from emergency import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drive', views.drive, name='drive'),
    path('staff', views.staff, name='staff'),
    path('staff/car', views.car_list, name='car_list'),
    path('staff/user', views.user_list, name='user_list'),
]
