from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! Now you can login.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request, profile_id):
    parameter = {
        'user': get_object_or_404(User, id=profile_id),
        'background_image': 'img/943545.jpeg',
    }
    return render(request, 'users/profile.html', parameter)


@login_required
def settings(request):
    if request.method == 'POST':
        form = UserProfileSettingsForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile settings updated successfully!')
            return redirect('profile', request.user.id)
    else:
        form = UserProfileSettingsForm(instance=request.user.profile)
    parameter = {
        'user': request.user,
        'background_image': 'img/943545.jpeg',
        'profile_form': form,
    }
    return render(request, 'users/settings.html', parameter)
