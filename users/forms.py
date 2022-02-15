"""The forms for the users app."""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user. This form is extend from the default Django UserCreationForm.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileSettingsForm(forms.ModelForm):
    """
    The form use in settings page to let user change their profile information in the settings page.
    """
    class Meta:
        model = Profile
        fields = ['image']