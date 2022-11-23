from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
