from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Spot(models.Model):
    spot_name = models.CharField(max_length=200)
    spot_address= models.CharField(max_length=400)
    spot_description= models.CharField(max_length=800)
    picture = models.ImageField(default='default.jpg', upload_to='spot_images')
    rating = models.IntegerField(default=0)
    
class Review(models.Model):
    link= models.ForeignKey(Spot, on_delete=models.CASCADE)
    text= models.CharField(max_length=800)
    
    
