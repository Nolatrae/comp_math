#pragma execution_character_set("utf-8")
print('выбор ответа [yes/no]')
print('Данные структурированы?')
a1 = input()
if (a1 == 'no'):
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
else:
    print('Данных много?')
    a8 = input()
    if (a8 =='yes'):
        print('Нагрузка смешанная?')
        a9 = input()
        if (a9 =='yes'):
            print('MongoDB')
        else:
            print('Нужен технологически независимый стек?')
            a10 = input()
            if(a10 == 'yes'):
                print('Нужна быстрая разработка?')
                a11 = input()
                if (a11 =='yes'):
                    print('Используется PHP?')
                    a12 = input()
                    if (a12 == 'yes'):
                        print('MySQL')
                    else:
                        print('PostgreSQL')
                else:
                    print('Есть сложные операции с данными?')
                    a13 = input()
                    if (a13 == 'yes'):
                        print('Есть администратор баз данных?')
                        a14 = input()
                        if(a14 == 'yes'):
                            print('PostgreSQL')
                        else:
                            print('MySQL')
                    else:
                        print('MySQL')
            else:
                print('Технологии Microsoft?')
                a15 = input()
                if (a15 == 'yes'):
                    print('MS SQL')
                else:
                    print('Yandex Database')
    else:
        print('Используются бессерверные вычисления?')
        a16 = input()
        if (a16 == 'yes'):
            print('Yandex Database')
        else:
                print('Нужна быстрая разработка?')
                a17 = input()
                if (a17 =='yes'):
                    print('Используется PHP?')
                    a18 = input()
                    if (a18 == 'yes'):
                        print('MySQL')
                    else:
                        print('PostgreSQL')
                else:
                    print('Есть сложные операции с данными?')
                    a19 = input()
                    if (a19 == 'yes'):
                        print('Есть администратор баз данных?')
                        a20 = input()
                        if(a20 == 'yes'):
                            print('PostgreSQL')
                        else:
                            print('MySQL')
                    else:
                        print('MySQL')

                    
