from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'skate'
urlpatterns = [
    path('', views.index, name='index'),
    path('signUp', views.signUp, name ='signUp'),
    path('signIn', views.signIn, name ='signIn'),
    path('logout', views.logout_view, name='logout'),
    path('addSpot', views.addSpot, name='addSpot'),
     path('spot/<pk>/', views.detail, name='detail'),
     path('spotedit/<pk>/', views.editSpot, name='edit'),
     path('reviewEdit/<pk>/', views.editReview, name='editReview'),
     path('reviewDelete/<pk>/', views.deleteReview, name='deleteReview'),
     path('spotDelete/<pk>/', views.deleteSpot, name='delete'),
     path('review/<pk>/', views.addReview, name='review')

    
    
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)