import argparse
import os

from bitlink.bitly import short_link


def get_dir_name(path):
    dir_name = '/'.join(path.split('/')[:-1])
    return dir_name


def create_dir(dir_name):
    os.makedirs(dir_name)


def enter_info(name, description, short_link, file_name):  # TODO ты передаешь file_name , но не используешь
    if name and description:
        if name:
            return f'{name} {description} - {short_link}'
        else:
            return f'{short_link}'
    else:
        if name:
            return f'{name} - {short_link}'
        else:
            return f'{description} - {short_link}'


def parse_console():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', help='URL адрес ресурса', required=True)
    parser.add_argument('-n', '--name', help='Имя ресурса')
    parser.add_argument('-d', '--description', help='Описание ресурса')
    parser.add_argument('-p', '--path', help='Путь логирования ресурса')

    args = parser.parse_args()

    return args.name, args.description, short_link(args.url), args.path
    # TODO давай вспомним про уровни асбстракции и принцип единой ответственности, совсем не ожидаем, что парс консоль
    #  внутри себя запускает short_link, обрезать надо в другом месте

# TODO тут вопрос к неймингу, почему файл называется cut_link,  хотя ничего про обрезание ссылки тут нет?
#  обычно всякую полезную всячину скидывают во что-то типа utils.py , ты можешь свой вариант придумать
