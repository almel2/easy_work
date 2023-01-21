import json
import time
import requests
from bs4 import BeautifulSoup as bs

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


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
    with open('vacancy_dict.json', 'w') as file:
        json.dump(data_dict, file, indent=4, ensure_ascii=False)


def validation_data(title, url, city, date, datekeyword='python', user_city=('kharkiv', 'Remote'), dict_data=[]):
    words_ignore = ['middle', 'mid', 'senior', 'data', 'vision',
                    'machine', 'full', 'mentor', 'commod', 'fullstack',
                    'cybersecurity', 'applied', 'solutions', 'lead']

    if title is None:
        title = 'None'
    if url is None:
        url = 'None'
    if city is None:
        city = 'None'
    if date is None:
        date = 'None'

    flag = True
    for item in words_ignore:
        if item in title.lower():
            flag = False
    if flag:
        dict_data.append(
            {
                'title': title,
                'url': url,
                'city': city,
                'date': date,
            }
        )
        write_in_file(dict_data)
