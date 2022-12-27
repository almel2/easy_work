import json

from url_requests import get_request_site_soup

url = 'https://jobs.dou.ua/vacancies/?search=python'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

data_dict = []

soup = get_request_site_soup(url, headers=headers)

all_title = soup.findAll('li', class_='l-vacancy')

for item in all_title:
    title = item.find('a', class_='vt').text.strip()
    url = item.find('a', class_='vt').get('href')
    city = item.find('span', {'class': 'cities'})
    date = item.find('div', class_='date')
    if date is not None:
        data_dict.append(
            {
                'title': title,
                'url': url,
                'city': city.text.strip(),
                'date': date.text.strip()
            }
        )

        with open('vacancy_dict.json', 'w') as file:
            json.dump(data_dict, file, indent=4, ensure_ascii=False)

    print(data_dict)
