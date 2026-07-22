
from django.contrib import admin
from django.urls import path
import myapp.views
urlpatterns = [
  path("",myapp.views.home), 
  path("about-us/",myapp.views.about),
  path("contact-us/",myapp.views.contact),
  path("dashboard/",myapp.views.dashboard),
  path("our-team/",myapp.views.team)
  
]