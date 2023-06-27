from django.contrib import admin
from .models import CreateFriend

class CreateFriendAdmin(admin.ModelAdmin):
    list_display = ["user", "userFriend", "id"]


admin.site.register(CreateFriend, CreateFriendAdmin) 