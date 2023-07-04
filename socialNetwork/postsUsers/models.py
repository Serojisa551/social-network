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
    good = models.IntegerField(default = 0)
    norm = models.IntegerField(default = 0)
    bad = models.IntegerField(default = 0)

    class Meta:
        db_table = 'post' 

    def getGood(self):
        good = self.good
        good += 1
        self.good = good
        self.save()

    def getNorm(self):
        norm = self.norm
        norm += 1
        self.norm = norm
        self.save()
        
    def getBad(self):
        bad = self.bad
        bad += 1
        self.bad = bad
        self.save()


