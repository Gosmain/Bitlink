import requests

def short_link(url):
  
  headers = {
    'Authorization': 'Bearer 7513bd6051bacfb260ef66a4a4ab35e27a74b683',
    'Content-Type': 'application/json',
}
  data = f'{{ "long_url": "{url}", "domain": "bit.ly"}}'

  response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

  return response.text
  

