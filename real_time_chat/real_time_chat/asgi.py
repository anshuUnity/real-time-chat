"""
ASGI config for real_time_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_time_chat.settings')

application = get_asgi_application()

ws_patterns = [
    
]


application=ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(
            ws_patterns
        ))
    }
)