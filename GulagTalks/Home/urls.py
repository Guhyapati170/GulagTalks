from django.urls import path
from Home.views import *

urlpatterns = [
    path('', home_view, name="home"),  
]
