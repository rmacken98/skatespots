from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
def index(request):
    return render(request, 'skate/index.html')

def detail(request):
    return render(request, 'skate/detail.html')
