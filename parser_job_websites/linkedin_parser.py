from parser_websites_jobs.url_requests import get_request_site_soup

url = 'https://www.linkedin.com/jobs/search/?keywords=Python&location=Ukraine&locationId=&geoId=102264497&f_TPR=r86400&f_WT=2&position=1&pageNum=0'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

soup = get_request_site_soup(url, headers=headers)

all_vacancies = soup.find('section', {'class': 'two-pane-serp-page__results-list'}).findAll('li')

for item in all_vacancies:
    title = item.find('a', {'class': 'base-card__full-link'}).text.strip()
    print(title)
    url = item.find('a', {'class': 'base-card__full-link'}).get('href')
    city = item.find('span', {'class': 'job-search-card__location'}).text.strip()
    date = item.find('time', {'class': 'job-search-card__listdate--new'}).text.strip()


