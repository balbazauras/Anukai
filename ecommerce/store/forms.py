from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Naudotojo Vardas")
    email = forms.EmailField(label="El. paštas")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Slaptažodis", help_text="Slaptažodį turi sudaryti bent 8 simboliai")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Pakartokite slaptažodį")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Naudotojo Vardas")
    password = forms.CharField(widget=forms.PasswordInput, label="Slaptažodis")