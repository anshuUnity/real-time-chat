from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import MobileNumber

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MobileNumberForm(forms.ModelForm):
    class Meta:
        model = MobileNumber
        fields = ['mobile_number']