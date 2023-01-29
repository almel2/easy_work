from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CastomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email adress'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
