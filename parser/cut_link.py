import argparse, os

def my_parser():

  parser = argparse.ArgumentParser()

  parser.add_argument('-u', '--url', type=str, help='URL адрес ресурса')
  parser.add_argument('-n', '--name', type=str, help='Имя ресурса')
  parser.add_argument('-d', '--description', type=str, help='Описание ресурса')
  parser.add_argument('-p', '--path', type=str, help='Путь логирования ресурса')

  args = parser.parse_args()

  if os.path.exists('/home/runner/Bitlink/parser/links')==False:
    os.mkdir('/home/runner/Bitlink/parser/links')

  if args.path:
    with open('parser/links/link.txt', 'a', encoding='utf-8') as file:
      file.write(f'{args.name} {args.description} - {args.url}\n')
      file.close

  print(f'{args.name} {args.description} - {args.url}')

