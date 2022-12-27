from url_requests import get_request_site_soup

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3392596455&distance=25&geoId=102264497&keywords=python'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

soup = get_request_site_soup(url, headers=headers)

all_vacancy = soup.findAll('div', {'class': 'flex-grow-1 artdeco-entity-lockup__content ember-view'})

print(all_vacancy)