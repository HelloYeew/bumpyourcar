"""The forms for the users app."""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout
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


class FirstLoginPromptForm(forms.Form):
    """
    The form in first setup page to let user set their detail on first setup
    """
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    personal_id = forms.IntegerField(required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = ['first_name', 'last_name', 'personal_id', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control-large'}),
        }
