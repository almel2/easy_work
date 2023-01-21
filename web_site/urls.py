from django.urls import path
from web_site import views

urlpatterns = [
    path('', views.VacanciesList.as_view(), name='vacancies_list'),
]