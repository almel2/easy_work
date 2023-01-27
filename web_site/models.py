from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class SiteModel(models.Model):
    site = models.CharField(_('Name_site'), max_length=255)

    def __str__(self):
        return self.site


class CityModel(models.Model):
    city = models.CharField(_('City'), max_length=255)

    def __str__(self):
        return self.city

class VacancyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey('web_site.SiteModel', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=511)
    url = models.URLField(_('URL'), max_length=511)
    city = models.ForeignKey('web_site.CityModel', on_delete=models.CASCADE)
    date = models.CharField(_('Date'), max_length=255)
    create_date = models.DateTimeField(_('Create date'), auto_now_add=True)

    def __str__(self):
        return self.title