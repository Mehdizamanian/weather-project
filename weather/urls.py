
from django.urls import path
from .views import WeatherView
app_name="weather"
urlpatterns = [
    path('',WeatherView , name="weatherview"),
]
