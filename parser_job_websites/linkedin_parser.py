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


def validation_title_on_keywords(title, keywords):
    for item in keywords:
        if item.lower() in title.lower():
            return True
    return False

def linkedin_parser(keyword):
    url = f'https://www.linkedin.com/jobs/search/?keywords={keyword}&location=Ukraine&locationId=&geoId=102264497&f_TPR=r86400&f_WT=2&position=1&pageNum=0'
    soup = get_request_site_soup(url)
    all_vacancies = soup.find('section', {'class': 'two-pane-serp-page__results-list'}).findAll('li')
    dict_data = []

    for item in all_vacancies:
        title = item.find('a', {'class': 'base-card__full-link'})
        if title is not None:
            title = title.text.strip()
            url = item.find('a', {'class': 'base-card__full-link'}).get('href')
            city = item.find('span', {'class': 'job-search-card__location'}).text.strip()
            date = item.find('time', {'class': 'job-search-card__listdate--new'})
            if date is None:
                date = 'None'
            else:
                date = date.text.strip()

            if validation_title_on_keywords(title, keyword):
                print(title)




print(linkedin_parser('python'))
