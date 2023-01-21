import requests


def robota_ua_parser(url='https://ua-api.rabota.ua/vacancy/search?keyWords=python&scheduleId=3&sortBy=Date'):
    res = requests.get(url)
    dict_data = []
    for item in res.json()['documents']:
        title = item['name']
        url = f"https://rabota.ua/ua/company{item['notebookId']}/vacancy{item['id']}"
        city = item['cityName']
        date = item['dateTxt']
        print(city)
        dict_data.append(
            {
                'title': title,
                'url': url,
                'city': city,
                'date': date,
            }
        )
    return dict_data

print(robota_ua_parser())