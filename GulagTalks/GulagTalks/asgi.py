"""
ASGI config for GulagTalks project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from Chat import routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GulagTalks.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({ 
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator (AuthMiddlewareStack(URLRouter(routing.websocket_urlpattern))
    )
})

ASGI_APPLICATION = 'GulagTalks.asgi.application'