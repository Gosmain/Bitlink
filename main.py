import requests

headers = {
    'Authorization': 'Bearer 7513bd6051bacfb260ef66a4a4ab35e27a74b683',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://kanikuli-v-meksike-tv.ru/2-sezon/56-seriya.html", "domain": "bit.ly"}'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

print(response.json()['id'])