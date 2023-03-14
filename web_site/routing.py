from django.urls import re_path

from web_site import consumers


websocket_urlpatterns = [
    re_path(r'', consumers.AllVacanciesConsumer.as_asgi())
]