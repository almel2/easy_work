import requests

from parser_job_websites.core_parser import Validation




def robota_ua_parser(url='https://ua-api.rabota.ua/vacancy/search?keyWords=python&scheduleId=3&sortBy=Date'):
    res = requests.get(url)
    for item in res.json()['documents']:
        title = item['name']
        print(title)
        url = f"https://rabota.ua/ua/company{item['notebookId']}/vacancy{item['id']}"
        city = item['cityName']
        date = item['dateTxt']
        validata = Validation('rabota_ua', title, url, city, date)
        validata.add_to_valid_data()
        valit_data = validata.valid_data
    #vac_list = AddToDatabase(1, validata)

    return valit_data

print(robota_ua_parser())