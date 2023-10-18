from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomizedUserCreationForm(UserCreationForm):
  first_name = forms.CharField(label="First Name", required=True)
  last_name = forms.CharField(label="Last Name", required=True)
  email = forms.EmailField(label="Email", required=True)
  
  class Meta:
    model = User
    fields = ("first_name", "last_name","email", "username", "password1", "password2")

    
 

  