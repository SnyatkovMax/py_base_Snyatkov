def word_count():
    print('Ввод слов, а после подсчет повторений слова')
    my_list = {}
    my_count = input('Введите слова >>> ').lower()
    if my_count.isspace():
        print('Слово не введено, программа завершена')
        quit()
    else:
        pass

    for i in my_count.replace(',', ' ').split():    # заменит запятые на пробелы между словами
        if i in my_list.keys():
            my_list[i] += 1
        else:
            my_list[i] = 1
    print(my_list)


word_count()
