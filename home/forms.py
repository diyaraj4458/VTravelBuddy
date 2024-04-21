# forms.py

from django import forms
from .models import Ride  # Import the Ride model
# from .models import RideListing

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure', 'destination', 'date', 'time', 'seats', 'price', 'mobile', 'description']
        