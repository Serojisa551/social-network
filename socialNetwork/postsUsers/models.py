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
    good = models.IntegerField(default=0)
    norm = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)
    reaction_user = models. OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reactions')

    class Meta:
        db_table = 'post'

    def getGood(self):
        if self.reaction_user is None:
            self.good += 1
            self.reaction_user = self.user
            self.save()
        else:
            raise ValueError("You have already placed a reaction on this post.")        
        
    def getNorm(self):
        if self.reaction_user is None:
            self.norm += 1
            self.reaction_user = self.user
            self.save()
        else:
            raise ValueError("You have already placed a reaction on this post.")

    def getBad(self):
        if self.reaction_user is None:
            self.bad += 1
            self.reaction_user = self.user
            self.save()
        else:
            raise ValueError("You have already placed a reaction on this post.")            
