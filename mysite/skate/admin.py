from django.contrib import admin
from .models import Spot
# Register your models here.

class SpotAdmin(admin.ModelAdmin):
    
    fieldsets= [
        (None,              {'fields': ['picture']})
    ]
    #inlines =[ChoiceInLine]
    list_display =('spot_name','spot_address')
    list_filter=['spot_name']
    search_fields = ['spot_name']

admin.site.register(Spot, SpotAdmin)






