import time
import requests
from bs4 import BeautifulSoup as bs


def get_request_site_soup(url_web_site, headers):
    counter = 0
    try:
        response = requests.get(url_web_site, headers=headers)
        soup = bs(response.text, 'lxml')
        return soup
    except ConnectionError as err:
        if counter < 5:
            counter += 1
            time.sleep(60)
            get_request_site_soup(url_web_site)
        raise SystemExit(err)
