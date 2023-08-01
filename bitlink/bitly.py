import requests
import os

my_secret = os.getenv('BITLY_TOKEN')

def short_link(url):
    headers = {
        'Authorization': f'Bearer {my_secret}',
        'Content-Type': 'application/json',
    }
    data = f'{{ "long_url": "{url}", "domain": "bit.ly"}}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    return response.text
