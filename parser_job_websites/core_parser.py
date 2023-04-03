import json
import os
import time
import random

import requests
from django.contrib.auth import get_user_model
from bs4 import BeautifulSoup as bs

from web_site.models import SiteModel, CityModel, VacancyModel, UserProfileModel

path_to_file = os.path.dirname(os.path.abspath(__file__))[:-19] + 'celery_app/' + 'vacancy_dict.json'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

User = get_user_model()


def get_request_site_soup(url):
    counter = 0
    try:
        response = requests.get(url, headers=headers)
        soup = bs(response.text, 'lxml')
        return soup
    except ConnectionError as err:
        if counter < 5:
            counter += 1
            time.sleep(60)
            get_request_site_soup(url)
        raise SystemExit(err)





class Validation:
    valid_data = []

    @staticmethod
    def validation_title_on_keywords(title, keywords):
        for item in keywords.split():
            if item.lower() in title.lower():
                return True
        return False

    @staticmethod
    def validation_title_on_words_ignore(title, words_ignore):
        flag = True
        for item in words_ignore:
            if item.lower() in title.lower():
                flag = False
        return flag

    def add_to_valid_data(self, site, title, url, city, date, keywords, words_ignore):
        site = site if site != None else 'No data'
        title = title if title != None else 'No data'
        url = url if url != None else 'No data'
        city = city if city != None else 'No data'
        date = date if date != None else 'No data'

        if self.validation_title_on_keywords(title, keywords):
            if self.validation_title_on_words_ignore(title, words_ignore):
                self.valid_data.append(
                    {
                        'site': site,
                        'title': title,
                        'url': url,
                        'city': city,
                        'date': date,
                    }
                )
        return self.valid_data


class AddToDatabase:
    def __init__(self, user_id, valid_data):
        self.user_id = user_id
        self.valid_data = valid_data
        self.vacancy_list = []

    def add_to_data(self):
        user = User.objects.get(pk=self.user_id)
        obj_user_profile, create = UserProfileModel.objects.update_or_create(user=user)
        if self.valid_data:
            for item in self.valid_data:
                obj_site, create = SiteModel.objects.get_or_create(site=item['site'])
                obj_city, create = CityModel.objects.get_or_create(city=item['city'])

                if obj_site.site == 'Linkedin':
                    vacancy_obj, update = VacancyModel.objects.update_or_create(
                        user=obj_user_profile,
                        title=item['title'],
                        city=obj_city,
                        site=obj_site,

                        defaults={'url': item['url'], 'date': item['date']}
                    )
                    if update:
                        self.vacancy_list.append(vacancy_obj)

                vacancy_obj, update = VacancyModel.objects.update_or_create(
                    user=obj_user_profile,
                    title=item['title'],
                    url=item['url'],
                    city=obj_city,
                    site=obj_site,

                    defaults={'date': item['date']}
                )
                if update:
                    self.vacancy_list.append(vacancy_obj)

        return self.vacancy_list
#
#
# class FakeVac:
#     def __init__(self, user, valid_data):
#         self.user = user
#         self.valid_data = valid_data
#         self.vacancy_list = []
#
#     def create_fake_vac(self):
#         site, created = SiteModel.objects.get_or_create(site='Easy Work')
#         city, created = CityModel.objects.get_or_create(city='Kharkiv / Южний')
#
#         fake_vac = VacancyModel.objects.create(
#             user=User.objects.get(pk=self.user),
#             title='Title number - ' + str(random.randint(1, 100)),
#             url='#',
#             city=city,
#             date='Here should be date',
#             site=site,
#         )
#         self.vacancy_list.append(fake_vac)
#         return self.vacancy_list
