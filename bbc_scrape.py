from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests

url = 'http://bbcsfx.acropolis.org.uk/?page='
page_num = 1
page_lim = 5 
# real page_limit
# page_lim = 641
results = []

response = requests.get(url, str(page_num))


'''
while page_num < page_lim:
    print(f'Getting page {page_num}')
    response = requests.get(url)
    results.append(response.text)
    page_num += 1
'''
