from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,reverse
from django.contrib import messages
from skate.models import Spot
from django.template import loader

def index(request):
    spot = Spot.objects.all()
    context ={'spot':spot}
    template = loader.get_template('skate/index.html')
    return HttpResponse(template.render(context, request))


def signIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        spot = Spot.objects.all()
        context ={'spot':spot}
        template = loader.get_template('skate/signUp.html')
        return HttpResponse(template.render(context, request))
    else:
          #if the the username and password do not match user is returned to home page with error message
          messages.warning(request, 'Invalid username or password.')
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
      # user is redirected to homepage with error message
          messages.warning(request, 'Username or Email had already been registered to a different account')
          print('username or email already registered')
          return HttpResponseRedirect(reverse('skate:index'))
    
    else:
          # user registration 
          user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
          user.save()
          login(request, user)
          messages.info(request, 'Registration complete')
          return HttpResponseRedirect(reverse('skate:signUp'))

def logout_view(request):
      #ends the session logs out the user and returns to homepage
      messages.info(request, 'Logout successful')
      logout(request)
      return HttpResponseRedirect(reverse('skate:index'))

def addSpot(request):
      print(request.FILES['picture'])
      spot= Spot(spot_name=request.POST['name'], spot_address=request.POST['address'], spot_description=request.POST['Description'],picture= request.FILES['picture'])
      spot.save()
      return render(request,'skate/signUp.html')