import os

from bitlink.bitly import short_link
from parser.my_parse_util import parse_console, get_dir_name, create_dir, enter_info

if __name__ == '__main__':

    args = parse_console()

    my_args = args.name, args.description, short_link(args.url)

    info = enter_info(my_args)
    if args.path:

        dir_name = get_dir_name(args.path)

        if not os.path.exists(dir_name):
            create_dir(dir_name)

        with open(args.path, 'a', encoding='utf-8') as f:
            f.write(f'{info}\n')

    print(info)
