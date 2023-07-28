import argparse
import os


def my_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', help='URL адрес ресурса', required=True)
    parser.add_argument('-n', '--name', help='Имя ресурса', required=True)
    parser.add_argument('-d', '--description', help='Описание ресурса', required=True)
    parser.add_argument('-p', '--path', help='Путь логирования ресурса')

    args = parser.parse_args()

    dir_name = '/'.join(args.path.split('/')[:-1])

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    if args.path:
        with open(f'{args.path}', 'a', encoding='utf-8') as file:
            file.write(f'{args.name} {args.description} - {args.url}\n')

    print(f'{args.name} {args.description} - {args.url}')
