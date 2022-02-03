from pdb import post_mortem
from pyexpat import model
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, models
from django.forms import fields
from django.forms.fields import EmailField

from store.models import Customer, ShippingAddress 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']