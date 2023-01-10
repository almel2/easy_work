import requests

from parser_websites_jobs.url_requests import get_request_site_soup



url = 'https://justjoin.it/api/offers/search?categories[]=Python'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

res = requests.get(url)

for item in res.json():
    title = item['title']
    url = 'https://justjoin.it/offers/' + item['id']
    city = item['workplace_type']
    date = item['published_at']

