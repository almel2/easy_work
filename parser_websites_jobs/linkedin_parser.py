from url_requests import get_request_site_soup

url = 'https://www.linkedin.com/jobs/search/?currentJobId=3420732022&f_TPR=r86400&geoId=102264497&keywords=python&location=Ukraine&refresh=true&sortBy=DD&position=16&pageNum=0'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

soup = get_request_site_soup(url, headers=headers)


def parser_linkedin(soup):

    all_vacancy = soup.findAll('div', {'class': 'base-card'})

    count = 0

    for i in all_vacancy:
        count += 1

    print(count)


parser_linkedin(soup)