import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

url = 'https://spb.rabota.ru/vacancy/?query=python&sort=relevance&all_regions=1'
jobs = []
errors = []
resp = requests.get(url, headers=headers)
domain = 'https://rabota.ru'

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', attrs={'class': 'home-vacancies__infinity-list'})
    div_lst = main_div.find_all('article', attrs={'itemscope': 'itemscope'})
    if div_lst:
        print('1')
    for div in div_lst:
        title = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).h3
        company = div.find('div', attrs={'class': 'vacancy-preview-card__company'}).a
        description = div.find('div', attrs={'class': 'vacancy-preview-card__short-description'})
        href = div.find('header', attrs={'class': 'vacancy-preview-card__header'}).a['href']
        jobs.append({'title': title.text, 'company': company.text, 'description': description.text, 'url': domain+href})

else:
    errors.append({'url': url, 'title': "Page don't response"})
    print('Errors:', errors)




h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()

