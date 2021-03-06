"""bumpyourcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(settings.ROOT_URL + 'admin/', admin.site.urls),
    path(settings.ROOT_URL, include('emergency.urls')),
    path(settings.ROOT_URL, include('users.urls')),
    path(settings.ROOT_URL + 'api/', include('api.urls')),
    path(settings.ROOT_URL + 'register/', user_views.register, name='register'),
    path(settings.ROOT_URL + 'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path(settings.ROOT_URL + 'logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Bump your car Administration'
admin.site.site_title = 'Bump your car'
admin.site.index_title = 'Bump your car Administration'
