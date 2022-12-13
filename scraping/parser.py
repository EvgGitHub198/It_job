import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

headers = [
{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv: 47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html, application/xhtmI+xmI,application/xml;q=0.9,*/*;q=0.8'},

{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xmI, application/xml;q=0.9,*/*;9=0.8'},

{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html, application/xhtml+xmI, application/xml;q=0.9,*/*;q=0.8'}
]



def hh(url):
    jobs = []
    errors = []
    url = 'https://hh.ru/search/vacancy?text=python&salary=&area=113&ored_clusters=true&enable_snippets=true'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'vacancy-serp-content'})
        if main_div:
            div_lst = main_div.find_all('div', class_='serp-item')
            for div in div_lst:
                title = div.find('h3')
                company = div.find('div', class_='bloko-text')
                description = main_div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
                href = main_div.find('div', attrs={'class': 'vacancy-serp-item-body__main-info'}).a['href']
                jobs.append({'title': title.text, 'company': company.text, 'description': description.text, 'url': href})

        else:
            errors.append({'url': url, 'title': "Div doesn't exist "})

    else:
        errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



def rabota(url):
    jobs = []
    errors = []
    domain = 'https://rabota.ru'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        nothing_jobs = soup.find('div', attrs={'class': 'vacancy-search-page__title-hint'})
        if not nothing_jobs:
            table = soup.find('div', attrs={'class': 'home-vacancies__infinity-list'})
            if table:
                div_lst = table.find_all('article', attrs={'itemscope': 'itemscope'})
                for div in div_lst:
                    title = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).h3
                    company = div.find('div', attrs={'class': 'vacancy-preview-card__company'}).a
                    description = div.find('div', attrs={'class': 'vacancy-preview-card__short-description'})
                    href = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).a['href']
                    jobs.append({'title': title.text, 'company': company.text, 'description': description.text,
                                 'url': domain + href})
            else:
                errors.append({'url': url, 'title': "Table doesn't exist "})
        else:
            errors.append({'url': url, 'title': "Page is empty"})

    else:
        errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



def yandex(url):
    jobs = []
    errors = []
    domain = 'https://yandex.ru'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        nothing_jobs = soup.find('div', attrs={'class': 'no-results-root-bWQVm'})
        if not nothing_jobs:
            main_div = soup.find('div', attrs={'class': 'lc-jobs-vacancies-list'})
            div_lst = main_div.find_all('span', attrs={'class': 'lc-jobs-vacancy-card'})
            for div in div_lst:
                title = div.find('div', attrs={
                    'class': 'lc-jobs-text lc-jobs-text_type_header lc-jobs-text_size_s lc-jobs-vacancy-card__header'}).find(
                    'div', attrs={'class': 'lc-styled-text'})
                description = div.find('div', attrs={
                    'class': 'lc-jobs-text lc-jobs-text_type_text lc-jobs-text_size_l lc-jobs-vacancy-card__description'}).find(
                    'div', attrs={'class': 'lc-styled-text'})
                href = div.find('a')['href']
                jobs.append(
                    {'title': title.text, 'company': 'Yandex', 'description': description.text, 'url': domain + href})


        else:
            errors.append({'url': url, 'title': "Page is empty"})

    else:
        errors.append({'url': url, 'title': "Page don't response"})

    return jobs, errors



# if __name__ == '__main__':
#     url = 'https://yandex.ru/jobs/vacancies/?text=python'
#     jobs, errors = yandex(url)
#     h = codecs.open('work.txt', 'w', 'utf-8')
#     h.write(str(jobs))
#     h.close()
