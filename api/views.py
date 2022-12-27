from rest_framework import viewsets
from web_site.models import VacancyModel
from api.serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = VacancyModel.objects.all()
    serializer_class = VacancySerializer
