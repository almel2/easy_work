import json

from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView

from celery_app.tasks import user_parser_for_keyword
from web_site.forms import UserKeywordForm
from web_site.models import VacancyModel

from django_celery_beat.models import PeriodicTask, IntervalSchedule

def index(request):
    return HttpResponse('Hello web site')


class VacanciesList(ListView):
    model = VacancyModel
    context_object_name = 'vacancies'
    template_name = 'web_site/vacancies_list.html'
    ordering = ('-create_date')


class UserParserKeyword(FormView):
    form_class = UserKeywordForm
    template_name = 'web_site/user_keyword.html'
    success_url = reverse_lazy('vacancies_list')

    def form_valid(self, form):
        keyword = form.data['keyword']
        user_id = self.request.user.id
        user_parser_for_keyword(keyword, user_id)
        # schedule, created = IntervalSchedule.objects.get_or_create(
        #     every=10,
        #     period=IntervalSchedule.MINUTES
        # )
        # PeriodicTask.objects.get_or_create(
        #     interval=schedule,
        #     name='user_parser_for_keyword',
        #     task='celery_app.tasks.user_parser_for_keyword',
        #     args=json.dumps([keyword]),
        #     start_time = timezone.now(),
        # )

        return super(UserParserKeyword, self).form_valid(form)


class UserParserKeywordCelery(FormView):
    form_class = UserKeywordForm
    template_name = 'web_site/user_keyword_celery.html'
    success_url = reverse_lazy('vacancies_list')

    def form_valid(self, form):
        keyword = form.data['keyword']
        user_object = self.request.user
        user_id = user_object.id
        user_email = user_object.email
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES
        )
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name=user_email + '_parser_for_keyword',
            task='celery_app.tasks.user_parser_for_keyword',
            args=json.dumps([keyword, user_id]),
            start_time = timezone.now(),
        )

        return super(UserParserKeywordCelery, self).form_valid(form)