# home.urls.py

from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path("",views.index,name='home'),
   path("about",views.about,name='about'),
   path("contact",views.contact,name='contact'),
   path("post_ride",views.post_ride,name='post_ride'),
   path("find_ride",views.find_ride,name='find_ride'),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
