from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"a.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def dashboard(request):
    return render(request,"dashboard.html")
    
def team(request):
    return render(request,"team.html")
    

   

   