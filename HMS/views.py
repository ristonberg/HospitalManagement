from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def login(request):
    return HttpResponse("Login")

def registration(request):
    return HttpResponse("Registration")

def homepage(request):
    return HttpResponse("Homepage")
