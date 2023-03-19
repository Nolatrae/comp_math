print('выбор ответа [yes/no]')
print('Данные структурированы?')
a1 = input()
if (a1 == 'yes'):
  print('Используется стек MEAN?')
  a2 = input()
  if(a2 == 'yes'):
    print('Основная цель - аналитические запросы?')
    a3 = input()
    if(a3 == 'yes'):
      print('Нужен ли полнотекстовый поиск?')
      a4 = input()
      if (a4 == 'yes'):
        print('Elasticsearch')
      else:
        print('Нужно изменять данные?')
        a5 = input()
        if (a5 == 'yes'):
          print('Elasticsearch')
        else:
          print('ClickHouse')
    else:
      print('Данных много?')
      a6 = input()
      if (a6 == 'yes'):
        print('MongoDB')
      else:
        print('Redis')
  else:
    print('Нужно изменять данные?')
    a7 = input()
    if (a7 == 'yes'):
      print('Elasticsearch')
    else:
      print('ClickHouse')