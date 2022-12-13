import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url = 'https://yandex.ru/jobs/vacancies/?text=python'
domain = 'https://yandex.ru'
jobs = []
errors = []
resp = requests.get(url, headers=headers)

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    nothing_jobs = soup.find('div', attrs={'class': 'no-results-root-bWQVm'})
    if not nothing_jobs:
        main_div = soup.find('div', attrs={'class': 'lc-jobs-vacancies-list'})
        div_lst = main_div.find_all('span', attrs={'class': 'lc-jobs-vacancy-card'})
        for div in div_lst:
            title = div.find('div', attrs={'class': 'lc-jobs-text lc-jobs-text_type_header lc-jobs-text_size_s lc-jobs-vacancy-card__header'}).find('div', attrs={'class': 'lc-styled-text'})
            description = div.find('div', attrs={'class': 'lc-jobs-text lc-jobs-text_type_text lc-jobs-text_size_l lc-jobs-vacancy-card__description'}).find('div', attrs={'class': 'lc-styled-text'})
            href = div.find('a')['href']
            jobs.append({'title': title.text, 'company': 'Yandex', 'description': description.text, 'url': domain+href})


    else:
        errors.append({'url': url, 'title': "Page is empty"})

else:
    errors.append({'url': url, 'title': "Page don't response"})



h = codecs.open('work3.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()