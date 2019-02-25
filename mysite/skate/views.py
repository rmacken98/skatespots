from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,reverse
def index(request):
    return render(request, 'skate/index.html')

def detail(request):
    return render(request, 'skate/detail.html')

def signIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print(user)
        return render(request,'skate/signUp.html')
    else:
          print("user does not exist")
          return HttpResponseRedirect(reverse('skate:index'))

def signUp(request):
    username = request.POST['username']
    password = request.POST['password']
    email= request.POST['email']
    user = authenticate(request, username=username,email=email, password=password)
    if user is not None:
      # the user has mistakenly tried to sign in with the sign up form if the username, email and password match it signs them in
        login(request, user)
      
        return render(request,'skate/signUp.html')
     
    elif User.objects.filter(username=username).exists() or  User.objects.filter(email=email).exists():
      # user has attempted to register with a username or email that already exists and 
      # their is no match between the username, email and password
          print('username or email already registered')
          return HttpResponseRedirect(reverse('skate:index'))
    
    else:
          # user registration 
          user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
          user.save()
          login(request, user)
          print(user)
          return HttpResponseRedirect(reverse('skate:signUp'))

def logout_view(request):
      logout(request)
      return HttpResponseRedirect(reverse('skate:index'))
