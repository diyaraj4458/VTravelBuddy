# models.py

from django.db import models

# makemigrations- create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=124)
    email= models.CharField( max_length=124)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    

class Ride(models.Model):
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mobile = models.CharField(max_length=20)
    description = models.TextField()

    def _str_(self):
        return f'Ride from {self.departure} to {self.destination} on {self.date} at {self.time}' 


class RideListing(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
#     # Add any additional fields specific to ride listings, such as ride status, rider preferences, etc.   
    