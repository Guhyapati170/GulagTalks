from django.urls import path, include
from .consumers import ChatroomConsumer

# Here, "" is routing to the URL ChatConsumer which 
# will handle the chat functionality.
websocket_urlpatterns = [
    path("ws/chatroom/<chatroom_name>" , ChatroomConsumer.as_asgi()) , 
]