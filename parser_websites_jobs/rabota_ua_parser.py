import json

from url_requests import get_request_site_soup

url = 'https://rabota.ua/ua/zapros/python/'


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


soup = get_request_site_soup(url, headers='')

print(soup)