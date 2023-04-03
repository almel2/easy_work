from parser_job_websites.core_parser import get_request_site_soup


def djinni_parser(url='https://djinni.co/jobs/?primary_keyword=Python&employment=remote'):
    soup = get_request_site_soup(url)
    all_vacancies = soup.find('div', {'class': 'row'}).findAll('li', {'class': 'list-jobs__item'})
    dict_data = []
    for item in all_vacancies:
        title = item.find('a', {'class': 'profile'}).text.strip()
        url = 'https://djinni.co' + item.find('a', {'class': 'profile'}).get('href')
        city = item.find('span', {'class': 'location-text'}).text.strip()
        date = item.find('div', {'class': 'text-date'}).text.strip().split()[0]
        dict_data.append(
            {
                'title': title,
                'url': url,
                'city': city,
                'date': date,
            }
        )
    print(dict_data)

djinni_parser()
