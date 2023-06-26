from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    photo = models.ImageField(upload_to="photoPosts/%Y/%m/%d/", null=True, blank=True)
    video = models.FileField(upload_to='videoPosts/%Y/%m/%d/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'post' 

    def __str__(self):
        return f"Post by {self.user.username}, {self.description}, {self.location}, {self.url}"

