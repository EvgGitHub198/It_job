import codecs

from scraping.parser import hh, rabota, yandex


parsers = (
    (hh, 'https://hh.ru/search/vacancy?text=python&salary=&area=113&ored_clusters=true&enable_snippets=true'),
    (rabota, 'https://rabota.ru/?query=python&sort=relevance'),
    (yandex, 'https://yandex.ru/jobs/vacancies/?text=python')
)

jobs, errors = [], []
for func, url in parsers: 
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
