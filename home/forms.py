# forms.py

from django import forms
from .models import Ride
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure', 'destination', 'date', 'time', 'seats', 'price', 'mobile', 'description', 'gender']

# forms.py
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
     