"""
ASGI config for easy_work project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import web_site.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easy_work.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        web_site.routing.websocket_urlpatterns,
    ),
})
