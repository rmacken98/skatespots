from django.db import models

# Create your models here.
class Spot(models.Model):
    spot_name = models.CharField(max_length=200)
    spot_address= models.CharField(max_length=400)
    spot_description= models.CharField(max_length=800)
    picture = models.ImageField(default='default.jpg', upload_to='spot_images')
   
    
