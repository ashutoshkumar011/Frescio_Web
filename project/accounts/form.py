from django import forms
from django.contrib.auth.models import User
from django.contrib.auth. forms import UserCreationForm

class UserRegisterForm (UserCreationForm): 

    phoneNo = forms.CharField()
    class Meta:
        model = User
        fields = ['phoneNo', 'password1', 'password2']