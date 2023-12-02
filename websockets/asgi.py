"""
ASGI config for websockets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from apps.message import consumers

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websockets.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Django's ASGI application to handle traditional HTTP requests
        "websocket": AuthMiddlewareStack(  # Defines the protocol type routing on websocket
            URLRouter(
                [
                    path(
                        "ws/messages/", consumers.MessageConsumer.as_asgi()
                    ),  # WebSocket chat handler
                ]
            )
        ),
    }
)
