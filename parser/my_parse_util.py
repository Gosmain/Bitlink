import argparse
import os


def get_dir_name(path):
    dir_name = '/'.join(path.split('/')[:-1])
    return dir_name


def create_dir(dir_name):
    os.makedirs(dir_name)


def comparison(comparison_object):
    return comparison_object if comparison_object else ''

def enter_info(data):
    name, description, short_link = list(map(comparison, data))
    return f'{name} {description} - {short_link}'.strip(' -')


def parse_console():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', help='URL адрес ресурса', required=True)
    parser.add_argument('-n', '--name', help='Имя ресурса')
    parser.add_argument('-d', '--description', help='Описание ресурса')
    parser.add_argument('-p', '--path', help='Путь логирования ресурса')

    args = parser.parse_args()

    return args
