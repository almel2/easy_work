import json
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_work.settings")
django.setup()
from celery import shared_task
from parser_job_websites.all_parsers import dou_ua_parser, djinni_parser, jastjoin_pl_parser, linkedin_parser, \
    robota_ua_parser, work_ua_parser
from web_site.models import VacancyModel

base_dir = os.path.dirname(__file__)


def add_new_data_in_bd():
    with open(os.path.join(base_dir, 'vacancy_dict.json')) as file:
        data = file.read()

    for item in json.loads(data):
        VacancyModel.objects.update_or_create(
            title=item['title'],
            url=item['url'],
            city=item['city'],
            date=item['date'],
        )


@shared_task
def celery_parser():
    dou_ua_parser()
    djinni_parser()
    robota_ua_parser()
    work_ua_parser()
    jastjoin_pl_parser()
    linkedin_parser()

    add_new_data_in_bd()
