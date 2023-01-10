import json
import requests
from url_requests import get_request_site_soup

url = 'https://www.work.ua/jobs-python/'


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


r = requests.get(url, headers=headers)

print(r.text)