import requests


def jastjoin_pl(url='https://justjoin.it/api/offers/search?categories[]=Python'):
    res = requests.get(url)

    for item in res.json():
        if item['workplace_type'] in ('partly_remote', 'office') or 'junior' not in item['title'].lower():
            continue
        title = item['title']
        url = 'https://justjoin.it/offers/' + item['id']
        city = item['workplace_type']
        date = item['published_at']




jastjoin_pl()