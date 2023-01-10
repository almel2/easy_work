from user_data import keyword
from parser_websites_jobs.url_requests import get_request_site_soup

url = 'https://www.work.ua/jobs-python/?days=122'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

soup = get_request_site_soup(url, headers=headers)

all_vacancies = soup.find('div', {'id': 'pjax-job-list'}).findAll('div', {'class': 'job-link'})

for item in all_vacancies:
    title = item.find('h2').text.strip()
    url = 'https://www.work.ua' + item.find('h2').find('a').get('href').strip()
    city = item.find('div', {'class': 'add-top-xs'}).find('span', {'class': 'middot'}).next_sibling.text.strip()
    date = item.find('h2').find('a').get('title').strip().split('від')[-1]
