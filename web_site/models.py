from django.db import models
from django.utils.translation import gettext_lazy as _


class VacancyModel(models.Model):
    title = models.CharField(_('Title'), max_length=511)
    url = models.URLField(_('URL'), max_length=511)
    city = models.CharField(_('City'), max_length=255)
    date = models.CharField(_('Date'), max_length=255)
    create_date = models.DateTimeField(_('Create date'), auto_now_add=True)