
from django.urls import path
from .views import LoginView,login_user

app_name="login"

urlpatterns = [
  path('',LoginView,name="loginview"),
  path('login_user/',login_user,name="login_user"),
  
]
