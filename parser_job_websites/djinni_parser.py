#from parser_job_websites.core_parser import get_request_site_soup
import requests
from bs4 import BeautifulSoup as bs
import time

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

def djinni_parser(url='https://djinni.co/jobs/?primary_keyword=Python&employment=remote'):
    soup = get_request_site_soup(url)
    all_vacancies = soup.find('div', {'class': 'row'}).findAll('li', {'class': 'list-jobs__item'})
    dict_data = []
    for item in all_vacancies:
        title = item.find('a', {'class': 'h3 job-list-item__link'}).text.strip()
        url = 'https://djinni.co' + item.find('a', {'class': 'h3 job-list-item__link'}).get('href')
        city = item.find('span', {'class': 'location-text'}).text.strip()
        date = item.find('span', {'class': 'mr-2 nobr'}).get('title')
        dict_data.append(
            {
                'title': title,
                'url': url,
                'city': city,
                'date': date,
            }
        )
    print(dict_data)

djinni_parser()
