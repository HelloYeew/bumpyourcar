from django.urls import path
from .views import *

urlpatterns = [
    path('post/location/<int:user_id>', update_user_location, name='update_user_location'),
]
