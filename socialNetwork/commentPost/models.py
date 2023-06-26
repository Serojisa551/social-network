from django.db import models
from postsUsers.models import Post
from django.contrib.auth.models import User


class CommentPost(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commandPost")
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commandPost")
    context = models.TextField()