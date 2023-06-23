from django.urls import path
from . import views



urlpatterns = [  
    path("command", views.createCommand, name="home"),
]