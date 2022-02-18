from django.urls import path
from users import views

urlpatterns = [
    path('profile/<int:profile_id>', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('setup', views.first_login_prompt, name='first_login_prompt')
]
