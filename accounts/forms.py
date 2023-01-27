from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CastomUser


class CastomUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CastomUser
        fields = ('email',)
