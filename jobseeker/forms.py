from django import forms
from django.contrib.auth.models import User
from django .contrib.auth.forms import UserCreationForm
from myapp.models import StudentProfile


class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","email","password1","password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        exclude=("user",)