from parser_job_websites.core_parser import get_request_site_soup


def work_ua_parser(url='https://www.work.ua/jobs-python/?days=122'):
    soup = get_request_site_soup(url)
    all_vacancies = soup.find('div', {'id': 'pjax-job-list'}).findAll('div', {'class': 'job-link'})

    for item in all_vacancies:
        title = item.find('h2').text.strip()
        url = 'https://www.work.ua' + item.find('h2').find('a').get('href').strip()
        city = item.find('div', {'class': 'add-top-xs'}).find('span', {'class': 'middot'}).next_sibling.text.strip()
        date = item.find('h2').find('a').get('title').strip().split('від')[-1]

