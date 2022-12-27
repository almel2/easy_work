import json
from django.core.management.base import BaseCommand
import os.path

from web_site.models import VacancyModel

BASE = os.path.dirname(os.path.abspath(__file__))


class Command(BaseCommand):
    help = 'This command create data'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(BASE, 'vacancy_dict.json')) as file:
                data = file.read()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'No such file or directory'))

        print(json.loads(data))

        counter = 0
        for item in json.loads(data):
            counter += 1
            VacancyModel.objects.update_or_create(
                title=item['title'],
                url=item['url'],
                city=item['city'],
                date=item['date'],
            )
            self.stdout.write(self.style.SUCCESS(f'Created data {counter}'))
        self.stdout.write(self.style.SUCCESS('Success create date!'))