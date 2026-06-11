

from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    return  HttpResponse("Welcome to Hosipital Appointment system")



def about(request):
    return render(request, "about.html")