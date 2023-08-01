import argparse
import os

def get_dir_name(path):
    dir_name = '/'.join(path.split('/')[:-1])
    return dir_name


def create_dir(dir_name):
    os.makedirs(dir_name)


def enter_info(date_tpl):
    name, description, short_link = date_tpl
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

    return args
    

