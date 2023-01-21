from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from web_site.models import VacancyModel

def index(request):
    return HttpResponse('Hello web site')


class VacanciesList(ListView):
    model = VacancyModel
    context_object_name = 'vacancies'
    template_name = 'web_site/vacancies_list.html'
