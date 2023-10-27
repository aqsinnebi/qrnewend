from django.contrib import admin

# Register your models here.
from . models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    list_display=['username', 'email', 'last_name','first_name']
    list_display_links=[ 'email', 'last_name','first_name']
    list_editable=['username' ]
    
    
    class Meta:
        model=CustomUser
