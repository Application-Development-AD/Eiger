from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import models
from django.forms import fields
from django.forms.fields import EmailField

from store.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password", "password2")