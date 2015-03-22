from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader

def login(request):
    return render(request, 'HMS/Login/login.html')

def registration(request):
    return render(request, 'HMS/Registration/registration.html')

def homepage(request):
    return HttpResponse("Homepage")

