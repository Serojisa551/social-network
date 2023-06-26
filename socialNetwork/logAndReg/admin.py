from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "id", "date_of_birth", "place_of_birth"]


admin.site.register(UserInfo, UserInfoAdmin) 