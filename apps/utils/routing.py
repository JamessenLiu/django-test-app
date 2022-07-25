"""
    Django channels routing.
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.modules.websockets import routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.WEBSOCKET_URLPATTERNS
        )
    ),
})
