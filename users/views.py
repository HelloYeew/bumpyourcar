from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FirstLogin
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


@login_required
def profile(request, profile_id):
    """
    The view for the profile page. User can view other user's profile too by using the profile ID.
    :param request: WSGI request from user.
    :param profile_id: The ID of the target user.
    :return: Render the page and pass the value from context to the template (profile.html)
    """
    profile = get_object_or_404(Profile, id=profile_id)
    if (request.user == profile.user) or request.user.is_superuser:
        parameter = {
            'profile': profile,
            'background_image': 'img/fuckinghelpme.png',
        }
        return render(request, 'users/profile.html', parameter)
    else:
        raise BadRequest('Invalid request.')


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
        'background_image': 'img/fuckinghelpme.png',
        'profile_form': form,
    }
    return render(request, 'users/settings.html', parameter)


@login_required
def first_login_prompt(request):
    """
    The view that view only render and appear when FirstLogin that bind with user is False.

    This page user will need to fill all of their information in order to finish this page.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (first_login_prompt.html).
    Will return redirect instead if the FirstLogin is True.
    """
    first_login_value = FirstLogin.objects.get(user=request.user)
    if first_login_value.first_login:
        return redirect('drive')
    else:
        if request.method == 'POST':
            form = FirstLoginPromptForm(request.POST)
            user_object = request.user
            profile_object = user_object.profile
            if form.is_valid():
                user_object.first_name = form.cleaned_data['first_name']
                user_object.last_name = form.cleaned_data['last_name']
                user_object.save()
                profile_object.personal_id = form.cleaned_data['personal_id']
                profile_object.address = form.cleaned_data['address']
                profile_object.save()
                first_login_value.first_login = True
                first_login_value.save()
                messages.success(request, f'Setup personal information successfully!')
                return redirect('drive')
        else:
            form = FirstLoginPromptForm()
        parameter = {
            'form': form,
        }
        return render(request, 'users/first_login_prompt.html', parameter)
