import json


from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os.path

from web_site.models import VacancyModel, CityModel, SiteModel, UserProfileModel

BASE = os.path.dirname(os.path.abspath(__file__))

User = get_user_model()


class Command(BaseCommand):
    help = 'This command create data'

    def handle(self, *args, **options):
        user = User.objects.get(pk=1)
        print(user)
        user_profile, create = UserProfileModel.objects.update_or_create(user=user)
        print(user_profile, 'prof')
        site, create = SiteModel.objects.update_or_create(site='Site foo')
        city, create = CityModel.objects.update_or_create(city='City foo')

        VacancyModel.objects.update_or_create(
                user=user_profile,
                title='title1',
                url='url1',
                city=city,
                date='Date 2',
                site=site,
                defaults={'date': 'Date 3'}
            )

        # try:
        #     with open(os.path.join(BASE, 'vacancy_dict.json')) as file:
        #         data = file.read()
        # except FileNotFoundError:
        #     self.stdout.write(self.style.ERROR(f'No such file or directory'))
        #
        #
        #
        # counter = 0
        # for item in json.loads(data):
        #     counter += 1
        #     site, create = SiteModel.objects.get_or_create(site=item['site'])
        #     city, create = CityModel.objects.get_or_create(city=item['city'])
        #
        #     VacancyModel.objects.update_or_create(
        #         user=User.objects.get(pk=1),
        #         title=item['title'],
        #         url=item['url'],
        #         city=city,
        #         date=item['date'],
        #         site=site,
        #     )
        #     self.stdout.write(self.style.SUCCESS(f'Created data {counter}'))
        self.stdout.write(self.style.SUCCESS('Success create date!'))