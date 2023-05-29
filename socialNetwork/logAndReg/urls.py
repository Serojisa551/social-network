from django.urls import path
from . import views

app_name = "logAndReg"   


urlpatterns = [
    path("", views.home, name="home"),
    path("registration", views.registration, name="registration"),
    path("login", views.login, name="login"),
    # path("password_reset/", views.password_reset_request, name="password_reset"),
]