import os

import requests

BITLY_TOKEN = os.getenv('BITLY_TOKEN')

def short_link(url):
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = f'{{ "long_url": "{url}", "domain": "bit.ly"}}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    return response.json()['link']

