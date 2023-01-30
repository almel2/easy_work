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

    # site, created = SiteModel.objects.get_or_create(site='Easy Work')
    # city, created = CityModel.objects.get_or_create(city='Kharkiv / Южний')
    # print(site)
    # VacancyModel.objects.create(
    #     user=User.objects.get(pk=user_id),
    #     title='На данный момент новых вакансий нет',
    #     url='#',
    #     city=city,
    #     date='Here should be date',
    #     site=site,
    # )

    for item in json.loads(data):
        site, create = SiteModel.objects.get_or_create(site=item['site'])
        city, create = CityModel.objects.get_or_create(city=item['city'])

        if site.site == 'Linkedin':
            print('work')
            VacancyModel.objects.update_or_create(
                user=User.objects.get(pk=user_id),
                title=item['title'],
                city=city,
                site=site,

                defaults={'url': item['url'], 'date': item['date']}
            )

        VacancyModel.objects.update_or_create(
            user=User.objects.get(pk=user_id),
            title=item['title'],
            url=item['url'],
            city=city,
            site=site,

            defaults={'date': item['date']}
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
