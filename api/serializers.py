from rest_framework import serializers

from web_site.models import VacancyModel


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = ['id', 'title', 'url', 'city', 'date', 'create_date']