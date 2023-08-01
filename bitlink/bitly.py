import os

import requests

my_secret = os.getenv('BITLY_TOKEN')


# TODO 1. константы пишем капсом
#  2. my_secret стремное название, не вижу смысла менять имя переменной, BITLY_TOKEN хорошее название


def short_link(url):
    headers = {
        'Authorization': f'Bearer {my_secret}',
        'Content-Type': 'application/json',
    }
    data = f'{{ "long_url": "{url}", "domain": "bit.ly"}}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    return response.json()['id']

# TODO посмотри что внутри JSON есть, точно id надо вернуть? Есть другое более подходящее поле
