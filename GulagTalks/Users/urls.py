from django.urls import path
from .views import profile_view,SignUP

urlpatterns = [
    path('', SignUP , name="Signing"),
] 

