import requests


def short_link(url):
    headers = {
        'Authorization': 'Bearer 7513bd6051bacfb260ef66a4a4ab35e27a74b683',
        # TODO ты хранишь токен в общем доступе, что позволяет любому зашедшему к тебе в гит ломануть тебя.
        # давай почитаем про окружение среды и .env, как хранить данные внутри .env и как получать к ним доступ
        # МОжешь посмотреть .gitignore там есть .env, то есть окружение среды не летит в гит)
        'Content-Type': 'application/json',
    }
    data = f'{{ "long_url": "{url}", "domain": "bit.ly"}}'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

    return response.text
