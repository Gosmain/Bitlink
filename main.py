import os

from parser.cut_link import parse_console, get_dir_name, create_dir, enter_info

if __name__ == '__main__':

    name, desc, link, file = parse_console()

    info = enter_info(name, desc, link, file)
    # TODO а если бы парс консол возвращал 10 значений ты бы 10 переменных в одной строке заводил?)
    #  Давай для удобства parse_console будет возвращать одну какую-то структуру, либо уже готовые аргс,
    #  либо сам определи в чем тебе их удобнее хранить
    #  энтер инфо пусть на вход так же принимает одну переменную, это в лучших практиках программирования,
    #  меньше на вход == лучше

    if file:

        dir_name = get_dir_name(file)

        if not os.path.exists(dir_name):
            create_dir(dir_name)

        with open(f'{file}', 'a', encoding='utf-8') as file:  # TODO насколько тут нужна фстрока?
            # TODO ты открываешь file и даешь ему алиас file :D Либо дай другой алиас, либо не давай вообще)
            file.write(f'{info}\n')

    print(info)
