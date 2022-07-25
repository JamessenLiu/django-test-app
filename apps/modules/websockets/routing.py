from django.conf.urls import url

from . import consumers

WEBSOCKET_URLPATTERNS = [
    url(r'^ws/(?P<socket_id>[^/]+)/$', consumers.DeployResult),
]