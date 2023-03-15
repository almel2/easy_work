import json
import os
import random

from django.contrib.auth import get_user_model

from api.serializers import VacancySerializer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_work.settings")

from celery import shared_task
from parser_job_websites.all_parsers import AllParserForUser
from web_site.models import VacancyModel, SiteModel, CityModel

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

base_dir = os.path.dirname(__file__)

User = get_user_model()


@shared_task(name='test_work_beat')
def test_work_beat():
    print('Success Beat is work!!!!!!!!!!!!!!!!!!')


def add_new_data_in_bd(user_id):
    vac_list = []
    with open(os.path.join(base_dir, 'vacancy_dict.json')) as file:
        data = file.read()

    site, created = SiteModel.objects.get_or_create(site='Easy Work')
    city, created = CityModel.objects.get_or_create(city='Kharkiv / Южний')

    fake_vac = VacancyModel.objects.create(
        user=User.objects.get(pk=user_id),
        title='Title number - ' + str(random.randint(1, 100)),
        url='#',
        city=city,
        date='Here should be date',
        site=site,
    )
    vac_list.append(fake_vac)

    for item in json.loads(data):
        site, create = SiteModel.objects.get_or_create(site=item['site'])
        city, create = CityModel.objects.get_or_create(city=item['city'])

        if site.site == 'Linkedin':
            VacancyModel.objects.update_or_create(
                user=User.objects.get(pk=user_id),
                title=item['title'],
                city=city,
                site=site,

                defaults={'url': item['url'], 'date': item['date']}
            )

        vacancy_obj, update = VacancyModel.objects.update_or_create(
            user=User.objects.get(pk=user_id),
            title=item['title'],
            url=item['url'],
            city=city,
            site=site,

            defaults={'date': item['date']}
        )
        if update:
            vac_list.append(vacancy_obj)


    channel_layer = get_channel_layer()

    serializer = VacancySerializer(vac_list, many=True).data
    async_to_sync(channel_layer.group_send)(
        'vacancy_updates',
        {
            'type': 'vacancy_update',
            'payload': serializer,
        }
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
