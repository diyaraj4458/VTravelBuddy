# admin.py

from django.contrib import admin
from home.models import Contact
from home.models import Ride

admin.site.register(Contact)
admin.site.register(Ride)


class RideAdmin(admin.ModelAdmin):
    list_display = ('departure', 'destination', 'date', 'time', 'seats', 'price', 'mobile', 'description')
    list_filter = ('date', 'time')
    search_fields = ('departure', 'destination')
    list_per_page = 20
