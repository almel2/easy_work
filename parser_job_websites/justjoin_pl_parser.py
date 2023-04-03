import requests


def jastjoin_pl(url='https://justjoin.it/api/offers/search?categories[]=Python'):
    res = requests.get(url)

    for item in res.json():
        if item['experience_level'] == 'junior' and item['workplace_type'] == 'remote':
            title = item['title']
            url = 'https://justjoin.it/offers/' + item['id']
            city = item['workplace_type']
            date = item['published_at']

            print(title)


jastjoin_pl()