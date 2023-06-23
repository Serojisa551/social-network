from django.contrib import admin
from .models import *

class CommentPostAdmin(admin.ModelAdmin):
    list_display = ["userId", "id", "postId", "context"]

admin.site.register(CommentPost, CommentPostAdmin)