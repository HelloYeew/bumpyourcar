from django.urls import path
from emergency import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drive', views.drive, name='drive'),
    path('staff', views.staff, name='staff'),
    path('staff/car', views.car_list, name='car_list'),
    path('staff/user', views.user_list, name='user_list'),
    path('staff/emergency', views.emergency_list, name='emergency_list'),
    path('staff/emergency/<int:car_id>', views.emergency_detail, name='emergency_detail'),
    path('staff/emergency/resolve/<int:car_id>', views.resolve_car, name='resolve_car'),
]
