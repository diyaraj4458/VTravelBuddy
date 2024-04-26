# views.py
from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from home.models import Contact 
from .forms import RideForm
from django.contrib import messages
from home.models import Ride
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
# Create your views here.
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

# def login(request):
#     return render(request, 'login.html')

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



@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html',{'form':form}) 

@auth
def dashboard_view(request):
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    return redirect('login')