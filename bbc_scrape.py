from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import time

from selenium import webdriver
browser = webdriver.Firefox()

url = 'http://bbcsfx.acropolis.org.uk/?page='
page_num = 1
page_lim = 641
results = []

for page in range(page_num, page_lim+1):
# iterate through pages
    # fetching page by page
    print(f'Getting page {page}')
    browser.get(url + str(page))

    # wait for the page to load
    time.sleep(5)

    if page != 641:
    # other than page 641, grab 25 labels and 25 urls to download per page
        for i in range(1,26):
            href = browser.find_element_by_xpath(f'/html/body/section/div/div/div[3]/table/tbody/tr[{i}]/td[5]/a')
            href = href.get_property('href')
            label = browser.find_element_by_xpath(f'/html/body/section/div/div/div[3]/table/tbody/tr[{i}]/td[1]')
            label = label.text
            print(f'appending ({href}, {label})')
            results.append((href, label))
    elif page == 641:
    # but on the last page, there are only 11 files
        for i in range(1,12): # hardcoded cuz we only have one endpage
            href = browser.find_element_by_xpath(f'/html/body/section/div/div/div[3]/table/tbody/tr[{i}]/td[5]/a')
            href = href.get_property('href')
            label = browser.find_element_by_xpath(f'/html/body/section/div/div/div[3]/table/tbody/tr[{i}]/td[1]')
            label = label.text
            print(f'appending ({href}, {label})')
            results.append((href, label))
    else:
        print('something is wrong with your if statement')
        
for i in range(len(results)):
    print(f'downloading file #{i}')
    url = results[i][0]
    # make spaces into underscores, delete comma and spaces
    filename = results[i][1].replace(' ', '_').replace(',', '').replace('.', '').lower()
    # delete slashes and brackets 
    filename = results[i][1].replace('/', '').replace('(', '').replace(')', '').lower()
    urlretrieve(url, f'downloaded/{filename}.wav')
    print(f'filename after formatting is {filename}')
