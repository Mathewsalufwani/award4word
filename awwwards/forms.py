from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from .models import *


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]