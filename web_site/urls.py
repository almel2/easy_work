from django.urls import path
from web_site import views

urlpatterns = [
    path('', views.VacanciesList.as_view(), name='vacancies_list'),
    path('index/', views.index, name='index'),
    path('keyword/', views.UserParserKeyword.as_view(), name='user_keyword'),
    path('keyword-celery/', views.UserParserKeywordCelery.as_view(), name='user_keyword_celery'),
]