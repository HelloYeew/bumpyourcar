from django.urls import path
from .views import *

urlpatterns = [
    path('location/<int:user_id>', user_location, name='user_location'),
    path('car/<int:car_id>', car_status, name='car_status'),
    path('car/full/<int:car_id>', get_car, name='get_car'),
    path('profile/<int:user_id>', get_profile, name='get_profile'),
    path('emergency/count', get_emergency_count, name='get_emergency_count'),
    path('emergency/list', get_emergency_list, name='get_emergency_list'),
]
