from django.urls import path
from .views import SpotListView,SpotDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'skate'
urlpatterns = [
    path('', SpotListView.as_view(), name='index'),
    path('signUp', views.signUp, name ='signUp'),
    path('signIn', views.signIn, name ='signIn'),
    path('logout', views.logout_view, name='logout'),
    path('addSpot', views.addSpot, name='addSpot'),
     path('spot/<pk>/', SpotDetailView.as_view(), name='detail')
    
    
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)