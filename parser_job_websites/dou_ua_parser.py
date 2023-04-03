from parser_job_websites.core_parser import get_request_site_soup, validation_data


def dou_ua_parser(url='https://jobs.dou.ua/vacancies/?remote&search=python%20'):
    soup = get_request_site_soup(url)
    all_title = soup.findAll('li', class_='l-vacancy')
    result = None
    for item in all_title:
        title = item.find('a', class_='vt').text.strip()
        url = item.find('a', class_='vt').get('href')
        city = item.find('span', {'class': 'cities'}).text.strip()
        date = item.find('div', class_='date')
        if date is None:
            date = 'None'
        else:
            date = date.text.strip()
        result = validation_data(title, url, city, date)

    return result

print(dou_ua_parser())
l = dou_ua_parser()
print(len(l))

