from django import forms

from .models import User

class RegisterForm(forms.Form):
    fullname = forms.CharField(max_length = 100, null = True)
    first_name = forms.CharField(max_length = 50, null = True)
    last_name = forms.CharField(max_length = 50, null = True)
    password = forms.CharField(max_length = 50,
            widget = forms.PasswordInput())
    email = forms.EmailField(widget = forms.EmailInput())

class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput())
    password = forms.CharField(max_length = 50,
            widget = forms.PasswordInput())
