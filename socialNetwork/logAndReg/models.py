from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models

class UserInfo(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    profile_picture = models.ImageField(upload_to="photosUsers/%Y/%m/%d/", null=True)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=128,null=True)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    
    class Meta:
        verbose_name = 'UserInfo' 
