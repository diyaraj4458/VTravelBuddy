# views.py
from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from home.models import Contact 
from .forms import RideForm
from django.contrib import messages
from home.models import Ride
# from .models import Ride
# from .forms import RideForm


# Create your views here.
def index(request):
    context = {
        "variable1":"Diya is Awesome",
        "variable2":"Daksha is cute"
    }
   
    return render(request, 'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email= email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')
   # return HttpResponse("This is contact page")



def post_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            # Create a Ride instance and save it to the database
            form.save()
            messages.success(request, "Your ride has been posted.")
            #return redirect('ride_detail', ride_id=ride.id)  # Redirect to a ride detail page

    else:
        form = RideForm()

    return render(request, 'post_ride.html', {'form': form})

def find_ride(request):
    rides = Ride.objects.all()
    departure = request.GET.get('departure')
    if departure:
        rides = rides.filter(departure__icontains=departure)
    
    # Filtering based on destination
    destination = request.GET.get('destination')
    if destination:
        rides = rides.filter(destination__icontains=destination)  # Case-insensitive filter

    # Filtering based on date
    date = request.GET.get('date')
    if date:
        rides = rides.filter(date=date)

    # Filtering based on time
    time = request.GET.get('time')
    if time:
        rides = rides.filter(time=time)

    return render(request, 'find_ride.html', {'rides': rides})

# def find_ride(request):
#     rides = Ride.objects.all()

#     if request.method == 'GET':
#         form = RideForm(request.GET)
#         if form.is_valid():
#             # Filter rides based on form data
#             departure = form.cleaned_data.get('departure')
#             destination = form.cleaned_data.get('destination')
#             date = form.cleaned_data.get('date')
#             time = form.cleaned_data.get('time')
            
#             if departure:
#                 rides = rides.filter(departure__icontains=departure)
#             if destination:
#                 rides = rides.filter(destination__icontains=destination)
#             if date:
#                 rides = rides.filter(date=date)
#             if time:
#                 rides = rides.filter(time=time)

#             # Render the template with the filtered and sorted rides
#             return render(request, 'find_ride.html', {'rides': rides, 'form': form})

#     # If the form is not submitted or invalid, render the template with all rides
#     form = RideForm()
#     return render(request, 'find_ride.html', {'rides': rides, 'form': form})




