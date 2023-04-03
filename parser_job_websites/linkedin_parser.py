from parser_job_websites.core_parser import get_request_site_soup, validation_title_on_keywords



def linkedin_parser(*args):
    url = 'https://www.linkedin.com/jobs/search?keywords=Python&location=Ukraine&locationId=&geoId=102264497&f_TPR=r86400&position=1&pageNum=0'
    soup = get_request_site_soup(url)
    all_vacancies = soup.find('section', {'class': 'two-pane-serp-page__results-list'}).findAll('li')
    dict_data = []
    keywords = args
    for item in all_vacancies:
        title = item.find('a', {'class': 'base-card__full-link'})
        if title is not None:
            title = title.text.strip()
            url = item.find('a', {'class': 'base-card__full-link'}).get('href')
            city = item.find('span', {'class': 'job-search-card__location'}).text.strip()
            date = item.find('time', {'class': 'job-search-card__listdate--new'})
            if date is None:
                date = 'None'
            else:
                date = date.text.strip()
            dict_data.append(
                {
                    'title': title,
                    'url': url,
                    'city': city,
                    'date': date,
                }
            )
    return dict_data


print(linkedin_parser('python', 'backend'))
print(len(linkedin_parser()))

