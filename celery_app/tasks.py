import json
import os

from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_work.settings")

from celery import shared_task
from parser_job_websites.all_parsers import AllParserForUser
from web_site.models import VacancyModel, SiteModel, CityModel

base_dir = os.path.dirname(__file__)

User = get_user_model()

@shared_task(name='test_work_beat')
def test_work_beat():
    print('Success Beat is work!!!!!!!!!!!!!!!!!!')


def add_new_data_in_bd(user_id):
    with open(os.path.join(base_dir, 'vacancy_dict.json')) as file:
        data = file.read()

    site, create = SiteModel.objects.get_or_create(site='My site Easy Work')
    city, create = CityModel.objects.get_or_create(city='Kharkiv')

    VacancyModel.objects.update_or_create(
        user=User.objects.get(pk=user_id),
        title='New test vacancy',
        url='#',
        city=city,
        date='Here should be date',
        site=site,
    )


    for item in json.loads(data):
        site, create = SiteModel.objects.get_or_create(site=item['site'])
        city, create = CityModel.objects.get_or_create(city=item['city'])

        VacancyModel.objects.update_or_create(
            user=User.objects.get(pk=user_id),
            title=item['title'],
            url=item['url'],
            city=city,
            date=item['date'],
            site=site,
        )



@shared_task
def user_parser_for_keyword(keyword, user_id):
    parser = AllParserForUser(keyword)

    parser.jastjoin_pl_parser()
    parser.dou_ua_parser()
    parser.djinni_parser()
    parser.work_ua_parser()
    parser.robota_ua_parser()
    parser.linkedin_parser()

    add_new_data_in_bd(user_id)
