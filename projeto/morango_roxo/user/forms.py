from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class FormRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password', 'password2']

class FormLogin(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']