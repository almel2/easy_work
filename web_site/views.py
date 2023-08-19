import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView, DetailView, TemplateView

from celery_app.tasks import user_parser_for_keyword
from web_site.forms import UserKeywordForm, KeywordForm, WordIgnoreForm
from web_site.models import VacancyModel, UserProfileModel

from django_celery_beat.models import PeriodicTask, IntervalSchedule


def index(request):
    return render(request, 'web_site/index.html')


class VacanciesList(ListView):
    model = VacancyModel
    context_object_name = 'vacancies'
    template_name = 'web_site/websocket_vacancies_list.html'
    ordering = ('-create_date',)





class UserProfile(TemplateView):
    template_name = 'web_site/profile.html'

    def get(self,request, *args, **kwargs):
        profile = UserProfileModel.objects.get(pk=request.user.id)
        keyword_form = KeywordForm()
        words_ignore = WordIgnoreForm()
        return self.render_to_response({'profile': profile, 'keyword_form': keyword_form, 'words_ignore': words_ignore})

    def post(self, request, *args, **kwargs):
        keyword_form = KeywordForm(
            request.POST, prefix='keyword'
        )
        words_ignore = WordIgnoreForm(
            request.POST, prefix='word_ignore'
        )
        if keyword_form.is_valid():
            keyword_form.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
        if words_ignore.is_valid():
            words_ignore.save()
            return HttpResponseRedirect(reverse_lazy('profile'))

        return self.render_to_response(
            self.get_context_data(keyword_form=keyword_form, words_ignore=words_ignore)
        )

class UserParserKeyword(LoginRequiredMixin, FormView):
    form_class = UserKeywordForm
    template_name = 'web_site/user_keyword.html'
    success_url = reverse_lazy('vacancies_list')

    def form_valid(self, form):
        keyword = form.data['keyword']
        user_id = self.request.user.id
        user_parser_for_keyword(keyword, user_id, ('front',))
        return super(UserParserKeyword, self).form_valid(form)


class UserParserKeywordCelery(LoginRequiredMixin, FormView):
    form_class = UserKeywordForm
    template_name = 'web_site/user_keyword_celery.html'
    success_url = reverse_lazy('vacancies_list')

    def form_valid(self, form):
        keyword = form.data['keyword']
        words_ignore = ('middle', 'mid', 'senior', 'data', 'vision',
                        'machine', 'full', 'mentor', 'commod', 'fullstack',
                        'cybersecurity', 'applied', 'solutions', 'lead',
                        'Викладач', 'Вчитель', 'QA', 'PHP')
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
            args=json.dumps([user_id, keyword, words_ignore]),
            start_time=timezone.now(),
        )

        return super(UserParserKeywordCelery, self).form_valid(form)
