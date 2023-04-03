import requests
from parser_job_websites.core_parser import get_request_site_soup, Validation


class AllParserForUser(Validation):

    def __init__(self, user_id, keywords, words_ignore=('front', 'middle', 'mid')):
        self.user_id = user_id
        self.keyword = keywords # need attantion !
        self.words_ignore = words_ignore

    def djinni_parser(self):
        url = f'https://djinni.co/jobs/?primary_keyword={self.keyword}&employment=remote'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('div', {'class': 'row'}).findAll('li', {'class': 'list-jobs__item'})
        site = 'Djinni.co'
        for item in all_vacancies:
            title = item.find('a', {'class': 'profile'}).text.strip()
            url = 'https://djinni.co' + item.find('a', {'class': 'profile'}).get('href')
            city = item.find('span', {'class': 'location-text'}).text.strip()
            date = item.find('div', {'class': 'text-date'}).text.strip().split()[0]

            self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)

    def dou_ua_parser(self):
        url = f'https://jobs.dou.ua/vacancies/?remote&search={self.keyword}%20'
        soup = get_request_site_soup(url)
        all_title = soup.findAll('li', class_='l-vacancy')
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

            self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)

    def jastjoin_pl_parser(self):
        url = f'https://justjoin.it/api/offers/search?categories[]={self.keyword}'
        res = requests.get(url)
        site = 'JastJoin_pl'

        for item in res.json():
            if item['experience_level'] == 'junior' and item['workplace_type'] == 'remote':
                title = item['title']
                url = 'https://justjoin.it/offers/' + item['id']
                city = item['workplace_type']
                date = item['published_at']

                self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)

    def linkedin_parser(self):
        url = f'https://www.linkedin.com/jobs/search/?keywords={self.keyword}&location=Ukraine&locationId=&geoId=102264497&f_TPR=r86400&f_WT=2&position=1&pageNum=0'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('section', {'class': 'two-pane-serp-page__results-list'}).findAll('li')
        site = 'Linkedin'

        for item in all_vacancies:
            title = item.find('a', {'class': 'base-card__full-link'})
            if title is not None:
                title = title.text.strip()
                url = item.find('a', {'class': 'base-card__full-link'}).get('href')
                city = item.find('span', {'class': 'job-search-card__location'}).text.strip()
                date = item.find('time', {'class': 'job-search-card__listdate--new'})
                date = date.text.strip() if date is not None else 'No data'

                self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)

    def robota_ua_parser(self):
        url = f'https://ua-api.rabota.ua/vacancy/search?keyWords={self.keyword}&scheduleId=3&sortBy=Date'
        res = requests.get(url)
        site = 'Robota.ua'

        for item in res.json()['documents']:
            title = item['name']
            url = f"https://rabota.ua/ua/company{item['notebookId']}/vacancy{item['id']}"
            city = item['cityName']
            date = item['dateTxt']

            self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)

    def work_ua_parser(self):
        url = f'https://www.work.ua/jobs-{self.keyword}/?days=122'
        soup = get_request_site_soup(url)
        all_vacancies = soup.find('div', {'id': 'pjax-job-list'}).findAll('div', {'class': 'job-link'})
        site = 'Work.ua'

        for item in all_vacancies:
            title = item.find('h2').text.strip()
            url = 'https://www.work.ua' + item.find('h2').find('a').get('href').strip()
            city = item.find('div', {'class': 'add-top-xs'}).find('span', {'class': 'middot'}).next_sibling.text.strip()
            date = item.find('h2').find('a').get('title').strip().split('від')[-1]

            self.add_to_valid_data(site, title, url, city, date, self.keyword, self.words_ignore)
