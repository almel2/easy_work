from api.serializers import VacancySerializer
from parser_job_websites.all_parsers import AllParserForUser
from parser_job_websites.core_parser import AddToDatabase
from celery import shared_task

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@shared_task(name='test_work_beat')
def test_work_beat():
    print('Success Beat is work!!!!!!!!!!!!!!!!!!')


@shared_task
def user_parser_for_keyword(user_id, keyword, words_ignore):
    parser = AllParserForUser(user_id, keyword, words_ignore)

    parser.jastjoin_pl_parser()
    parser.dou_ua_parser()
    parser.djinni_parser()
    parser.work_ua_parser()
    parser.robota_ua_parser()
    parser.linkedin_parser()

    valid_data = parser.valid_data

    database = AddToDatabase(user_id, valid_data)
    database.add_to_data()
    vac_list = database.vacancy_list

    if vac_list:
        channel_layer = get_channel_layer()
        serializer = VacancySerializer(vac_list, many=True).data
        async_to_sync(channel_layer.group_send)(
            'vacancy_updates',
            {
                'type': 'vacancy_update',
                'payload': serializer,
            }
        )
