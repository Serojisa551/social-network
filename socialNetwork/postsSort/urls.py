from django.urls import path
from .views import *

urlpatterns = [
    path("frineds's/<int:userId>/", friendsPostsSorter),
    path("newPosts", sortPostsByTime),
]
