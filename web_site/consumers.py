import json

from channels.generic.websocket import AsyncWebsocketConsumer, AsyncConsumer
from channels.db import database_sync_to_async
from web_site.models import VacancyModel
from api.serializers import VacancySerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class AllVacanciesConsumer(AsyncWebsocketConsumer):
    user = None

    async def connect(self):
        await self.accept()

        await self.channel_layer.group_add('vacancy_updates', self.channel_name)

        vacancies = await self.get_all_vacancies()
        print('work all vac !!!!!!!!!!!!--------------------')
        await self.send(text_data=json.dumps(vacancies))

    @database_sync_to_async
    def get_all_vacancies(self):
        vacancies = VacancyModel.objects.all().order_by('-create_date')
        serializer = VacancySerializer(vacancies, many=True).data
        return serializer

    async def vacancy_update(self, event):
        print('------------------------work consumer !!!!!')
        await self.send(text_data=json.dumps(event['payload']))

        vacancies = await self.get_all_vacancies()
        await self.send(text_data=json.dumps(vacancies))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
