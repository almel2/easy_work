from django.urls import path
from web_site import views

urlpatterns = [
    path('', views.index, name='home'),
]