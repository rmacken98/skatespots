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
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print('user already exists')
        return render(request,'skate/index.html')
        
    else:
          user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
          user.save()
          print(user)
          return HttpResponseRedirect(reverse('skate:signUp'))

def logout_view(request):
      logout(request)
      return HttpResponseRedirect(reverse('skate:index'))