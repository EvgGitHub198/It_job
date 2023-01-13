import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

headers = [
{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv: 47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html, application/xhtml+xmI,application/xml;q=0.9,*/*;q=0.8'},

{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xmI, application/xml;q=0.9,*/*;9=0.8'},

{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html, application/xhtml+xmI, application/xml;q=0.9,*/*;q=0.8'}
]



def hh(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'vacancy-serp-content'})
            if main_div:
                div_lst = main_div.find_all('div', class_='serp-item')
                for div in div_lst:
                    title = div.find('h3')
                    company = div.find('div', class_='bloko-text')
                    description = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
                    if description:
                        href = div.find('a')['href']
                        jobs.append({'title': title.text, 'company': company.text, 'description': description.text, 'url': href,
                                     'city_id': city, 'language_id': language})


            else:
                errors.append({'url': url, 'title': "Div doesn't exist "})

        else:
            errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



def rabota(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://rabota.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            nothing_jobs = soup.find('div', attrs={'class': 'vacancy-search-page__title-hint'})
            if not nothing_jobs:
                table = soup.find('div', attrs={'class': 'infinity-scroll r-serp__infinity-list'})
                if table:
                    div_lst = table.find_all('article', attrs={'itemscope': 'itemscope'})
                    for div in div_lst:
                        title = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).h3
                        company = div.find('div', attrs={'class': 'vacancy-preview-card__company'}).a
                        description = div.find('div', attrs={'class': 'vacancy-preview-card__short-description'})
                        href = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).a['href']
                        jobs.append({'title': title.text, 'company': company.text, 'description': description.text,
                                     'url': domain + href, 'city_id': city, 'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Table doesn't exist "})
            else:
                errors.append({'url': url, 'title': "Page is empty"})

        else:
            errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



def yandex(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://yandex.ru'
    if url:

        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            nothing_jobs = soup.find('div', attrs={'class': 'no-results-root-bWQVm'})
            if not nothing_jobs:
                main_div = soup.find('div', attrs={'class': 'lc-jobs-vacancies-list'})
                div_lst = main_div.find_all('span', attrs={'class': 'lc-jobs-vacancy-card'})
                for div in div_lst:
                    title = div.find('div', attrs={
                        'class': 'lc-jobs-text lc-jobs-text_type_header lc-jobs-text_size_s lc-jobs-vacancy-card__header'}).find('div', attrs={'class': 'lc-styled-text'})
                    description = div.find('div', attrs={
                        'class': 'lc-jobs-text lc-jobs-text_type_text lc-jobs-text_size_l lc-jobs-vacancy-card__description'}).find('div', attrs={'class': 'lc-styled-text'})
                    href = div.find('a')['href']
                    jobs.append(
                        {'title': title.text, 'company': 'Yandex', 'description': description.text, 'url': domain + href,
                         'city_id': city, 'language_id': language})


            else:
                errors.append({'url': url, 'title': "Page is empty"})

        else:
            errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



# if __name__ == '__main__':
#     url = 'https://spb.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&excluded_text=&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50'
#     jobs, errors = hh(url)
#     h = codecs.open('work.txt', 'w', 'utf-8')
#     h.write(str(jobs))
#     h.close()
