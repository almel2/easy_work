import requests

url = 'https://ua-api.rabota.ua/vacancy/search?keyWords=python&scheduleId=3&sortBy=Date'

res = requests.get(url)

for item in res.json()['documents']:
    title = item['name']
    url = item['designBannerUrl']
    city = f"https://rabota.ua/ua/company{item['notebookId']}/vacancy{item['id']}"
    date = item['dateTxt']
