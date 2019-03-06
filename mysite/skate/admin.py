from django.contrib import admin
from .models import Spot,Review
# Register your models here.

class SpotAdmin(admin.ModelAdmin):
    
    fieldsets= [
        (None,              {'fields': ['picture']})
    ]
    #inlines =[ChoiceInLine]
    list_display =('spot_name','spot_address','spot_description','picture','rating','author')
    list_filter=['spot_name']
    search_fields = ['spot_name']


class ReviewAdmin(admin.ModelAdmin):
    
    fieldsets= [
        (None,              {'fields': ['text']})
    ]
    #inlines =[ChoiceInLine]
    list_display =('link','text','pub_date','author')
    list_filter=['author','pub_date']
    search_fields = ['author']





admin.site.register(Spot, SpotAdmin)
admin.site.register(Review, ReviewAdmin)






