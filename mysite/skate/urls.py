from django.urls import path

from . import views

app_name = 'skate'
urlpatterns = [
    path('', views.index, name='index'),
    path('/signUp', views.detail, name ='detail')
    
]