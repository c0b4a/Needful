#!/usr/bin/env python
'''scraper5000.py: connects to page and prints text'''

#imports
import requests

def get_page(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        #returns html
        return response
    else:
        return None

#main
URL = "https://example.com"
page = get_page(URL)

if page.text:
    print(page.text)
else:
    print('Error: No text located on page')
