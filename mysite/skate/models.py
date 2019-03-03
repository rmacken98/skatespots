from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Spot(models.Model):
    spot_name = models.CharField(max_length=200)
    spot_address= models.CharField(max_length=400)
    spot_description= models.CharField(max_length=800)
    picture = models.ImageField(upload_to='media/Images/')
   
    
