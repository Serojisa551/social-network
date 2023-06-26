from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["username","id", "email"]



class PostAdmin(admin.ModelAdmin):

    list_display = ["user","id", "description", "location", "url"]


admin.site.unregister(User)  
admin.site.register(User, UserAdmin) 
admin.site.register (Post, PostAdmin)