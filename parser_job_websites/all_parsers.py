import requests
from parser_job_websites.bs4_requests import get_request_site_soup, validation_data


class AllParserForUser:
    dict_data = []

    def __init__(self, keyword='python', city='Kharkiv'):
        self.keyword = keyword
        self.city = city

    def djinni_parser(self):
        url = f'https://djinni.co/jobs/?primary_keyword={self.keyword}&employment=remote'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('div', {'class': 'row'}).findAll('li', {'class': 'list-jobs__item'})
        resutl = None
        site = 'Djinni.co'
        for item in all_vacancies:
            title = item.find('a', {'class': 'profile'}).text.strip()
            url = 'https://djinni.co' + item.find('a', {'class': 'profile'}).get('href')
            city = item.find('span', {'class': 'location-text'}).text.strip()
            date = item.find('div', {'class': 'text-date'}).text.strip().split()[0]

            resutl = validation_data(title, url, city, date, site)

        return resutl

    def dou_ua_parser(self):
        url = f'https://jobs.dou.ua/vacancies/?remote&search={self.keyword}%20'
        soup = get_request_site_soup(url)
        all_title = soup.findAll('li', class_='l-vacancy')
        result = None
        site = 'Dou.ua'
        for item in all_title:
            title = item.find('a', class_='vt').text.strip()
            url = item.find('a', class_='vt').get('href')
            city = item.find('span', {'class': 'cities'}).text.strip()
            date = item.find('div', class_='date')
            if date is None:
                date = 'None'
            else:
                date = date.text.strip()

            result = validation_data(title, url, city, date, site)

        return result

    def jastjoin_pl_parser(self):
        url = f'https://justjoin.it/api/offers/search?categories[]={self.keyword}'
        res = requests.get(url)
        resutl = None
        site = 'JastJoin_pl'
        for item in res.json():
            if item['workplace_type'] in ('partly_remote', 'office') or 'junior' not in item['title'].lower():
                continue
            title = item['title']
            url = 'https://justjoin.it/offers/' + item['id']
            city = item['workplace_type']
            date = item['published_at']
            resutl = validation_data(title, url, city, date, site)

        return resutl

    def linkedin_parser(self):
        url = f'https://www.linkedin.com/jobs/search/?keywords={self.keyword}&location=Ukraine&locationId=&geoId=102264497&f_TPR=r86400&f_WT=2&position=1&pageNum=0'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('section', {'class': 'two-pane-serp-page__results-list'}).findAll('li')
        resutl = None
        site = 'Linkedin'
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

                resutl = validation_data(title, url, city, date, site)

        return resutl

    def robota_ua_parser(self):
        url = f'https://ua-api.rabota.ua/vacancy/search?keyWords={self.keyword}&scheduleId=3&sortBy=Date'
        res = requests.get(url)
        resutl = None
        site = 'Robota.ua'
        for item in res.json()['documents']:
            title = item['name']
            url = f"https://rabota.ua/ua/company{item['notebookId']}/vacancy{item['id']}"
            city = item['cityName']
            date = item['dateTxt']

            resutl = validation_data(title, url, city, date, site)

        return resutl

    def work_ua_parser(self):
        url = f'https://www.work.ua/jobs-{self.keyword}/?days=122'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('div', {'id': 'pjax-job-list'}).findAll('div', {'class': 'job-link'})
        resutl = None
        site = 'Work.ua'
        for item in all_vacancies:
            title = item.find('h2').text.strip()
            url = 'https://www.work.ua' + item.find('h2').find('a').get('href').strip()
            city = item.find('div', {'class': 'add-top-xs'}).find('span', {'class': 'middot'}).next_sibling.text.strip()
            date = item.find('h2').find('a').get('title').strip().split('??????')[-1]

            resutl = validation_data(title, url, city, date, site)

        return resutl
