from django.contrib.auth.forms import UsernameField
from django.db import models
from django.forms.fields import EmailField

# Create your models here.
class Account(models.Model):
    email = models.EmailField(default=None)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []