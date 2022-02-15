from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *


def register(request):
    """
    The view for the register page.
    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (register.html)
    """
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
    """
    The view for the profile page. User can view other user's profile too by using the profile ID.
    :param request: WSGI request from user.
    :param profile_id: The ID of the target user.
    :return: Render the page and pass the value from context to the template (profile.html)
    """
    parameter = {
        'profile': get_object_or_404(Profile, id=profile_id),
        'background_image': 'img/943545.jpeg',
    }
    return render(request, 'users/profile.html', parameter)


@login_required
def settings(request):
    """
    The view for the settings page. User can change their profile information here.
    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (settings.html)
    """
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
