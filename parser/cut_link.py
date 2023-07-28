import argparse, os


def my_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', '--url', help='URL адрес ресурса')
    parser.add_argument('-n', '--name', help='Имя ресурса')
    parser.add_argument('-d', '--description', help='Описание ресурса')
    parser.add_argument('-p', '--path', help='Путь логирования ресурса')

    args = parser.parse_args()

    name_link_file = args.path.split('/')
    name_dir = '/'.join(name_link_file[:-1])
    name_file = name_link_file[-1]

    if not os.path.exists(f'{name_dir}'):  # TODO убрать фстроки
        os.makedirs(f'{name_dir}')

    if args.path:
        with open(f'{name_dir}/{name_file}', 'a', encoding='utf-8') as file:
            # TODO убрать фстроку и изменить путь на полный из аргов
            file.write(f'{args.name} {args.description} - {args.url}\n')
            # TODO что будет, если в параметрах не передали имя?
            file.close
            # TODO не вызов функции, почитать про контекстный менеджер with,
            #  и разобраться как он работает для open(), убрать после этого лишнюю строчку кода

    print(f'{args.name} {args.description} - {args.url}')

    # TODO ты как программист после того, как что-то написал должен убедиться, что твое решение работает
    #  запусти программу с разными параметрами и убедись,
    #  что она работает согласно бизнес-логике, пока что много падений

    # TODO разбить my_parser() на маленькие ниверсальные функции,
    #  переименовать переменные name_... на ..._name
