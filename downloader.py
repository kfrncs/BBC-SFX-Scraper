from urllib.request import urlretrieve
import requests
import time
import pickle
import os

start = time.time()

print('opening pickle')
with open('list.pkl', 'rb') as f:
    results = pickle.load(f)

print('starting loop')
for i in range(len(results)):
    url = results[i][0]
    # make spaces into underscores, delete comma and spaces
    filename = results[i][1].replace(' ', '_').replace(',', '').replace('.', '').lower()
    # delete slashes and brackets
    filename = filename.replace('/', '').replace('(', '').replace(')', '').lower()

    print(f'downloading file #{i+1}:')
    print(f'{filename}.wav')
    urlretrieve(url, f'downloaded/{filename}.wav')
    now = time.time()
    print(f'time elapsed: {int((now - start)//60)}min {int((now - start) % 60)}sec')
