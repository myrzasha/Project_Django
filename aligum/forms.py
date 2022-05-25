from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')