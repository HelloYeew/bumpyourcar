from django.contrib import admin
from django.urls import path

from emergency import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='home')
]
