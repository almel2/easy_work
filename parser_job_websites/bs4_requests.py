import json
import os
import time
import requests
from bs4 import BeautifulSoup as bs

path_to_file = os.path.dirname(os.path.abspath(__file__))[:-19] + 'celery_app/' + 'vacancy_dict.json'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


class RequestAndGetSoup:
    pass


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


def write_in_file(data_dict):
    with open(path_to_file, 'w') as file:
        json.dump(data_dict, file, indent=4, ensure_ascii=False)


def validation_title_on_keywords(title):
    keywords = ('python', 'back', 'django')

    for item in keywords:
        if item.lower() in title.lower():
            return True

    return False


def validation_data(title, url, city, date, site, keyword='python', user_city=('kharkiv', 'Remote'), dict_data=[]):
    words_ignore = ('middle', 'mid', 'senior', 'data', 'vision',
                    'machine', 'full', 'mentor', 'commod', 'fullstack',
                    'cybersecurity', 'applied', 'solutions', 'lead',
                    'Викладач', 'Вчитель', 'QA', 'PHP')

    if title is None:
        title = 'None'
    if url is None:
        url = 'None'
    if city is None:
        city = 'None'
    if date is None:
        date = 'None'

    flag = True
    for item in words_ignore:   # This valid ignore vacancies from words_ignore
        if item.lower() in title.lower():
            flag = False


    if flag:
        if validation_title_on_keywords(title):
            dict_data.append(
                {
                    'site': site,
                    'title': title,
                    'url': url,
                    'city': city,
                    'date': date,
                }
            )
            write_in_file(dict_data)


class Validation:
    pass


class ValidationUserKeyword:
    pass


class ValidationDataFromParser:
    pass


class ValidationTitleFromVacancy:
    pass