from django.urls import path
from . import views

app_name = "logAndReg"   


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("reset/", views.reset_password, name="reset_password"),
]