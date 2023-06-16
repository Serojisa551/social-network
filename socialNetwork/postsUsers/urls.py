from django.urls import path
from .views import PostCreateView

urlpatterns = [
    path("post", PostCreateView.as_view(), name="posts")
]