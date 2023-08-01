from parser.cut_link import parse_console, get_dir_name, create_dir, enter_info
import os

if __name__ == '__main__':

  name, desc, link, file =  parse_console()

  info = enter_info(name, desc, link, file)

  if file:

    dir_name = get_dir_name(file)

    if not os.path.exists(dir_name):
      create_dir(dir_name)
    with open(f'{file}', 'a', encoding='utf-8') as file:
      file.write(f'{info}\n')

  print(info)
  



