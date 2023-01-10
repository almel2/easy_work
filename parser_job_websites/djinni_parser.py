from parser_websites_jobs.url_requests import get_request_site_soup

url = 'https://djinni.co/jobs/?primary_keyword=Python&employment=remote'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


soup = get_request_site_soup(url, headers=headers)

all_vacancies = soup.find('div', {'class': 'row'}).findAll('li', {'class': 'list-jobs__item'})

for item in all_vacancies:
    title = item.find('a', {'class': 'profile'}).text.strip()
    url = 'https://djinni.co' + item.find('a', {'class': 'profile'}).get('href')
    city = item.find('span', {'class': 'location-text'}).text.strip()
    date = item.find('div', {'class': 'text-date'}).text.strip().split()
    print(date)
