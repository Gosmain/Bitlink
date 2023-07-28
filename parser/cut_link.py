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

  if not os.path.exists(f'{name_dir}'):
    os.makedirs(f'{name_dir}')

  if args.path:
    with open(f'{name_dir}/{name_file}', 'a', encoding='utf-8') as file:
      file.write(f'{args.name} {args.description} - {args.url}\n')
      file.close

  print(f'{args.name} {args.description} - {args.url}')



