from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import CastomUserForm


class Register(FormView):
    form_class = CastomUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('user_keyword_celery')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(Register, self).form_valid(form)
