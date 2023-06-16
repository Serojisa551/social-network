from django.contrib import admin
from .models import *
from logAndReg.models import User

class PostAdmin(admin.ModelAdmin):

    list_display = ["user", "description", "location", "url"]



admin.site.register (Post, PostAdmin)