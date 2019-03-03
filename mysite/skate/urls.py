from django.urls import path
from .views import SpotListView,SpotDetailView
from . import views

app_name = 'skate'
urlpatterns = [
    path('', SpotListView.as_view(), name='index'),
    path('signUp', views.signUp, name ='signUp'),
    path('signIn', views.signIn, name ='signIn'),
    path('logout', views.logout_view, name='logout'),
    path('addSpot', views.addSpot, name='addSpot'),
     path('spot/<pk>/', SpotDetailView.as_view(), name='detail')
    
    
    
]