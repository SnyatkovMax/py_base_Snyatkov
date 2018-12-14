def sort_words():
    print('Программа для сортировки слов из текста без повторений')
    my_list = {}
    my_count = input('Введите слова >>> ').lower()
    if my_count.isspace():
        print('Слово не введено, программа завершена')
        quit()
    else:
        pass

    for i in my_count.replace(',', ' ').split():  # заменит запятые на пробелы между словами
        if i in my_list.keys():
            my_list[i] += 1
        else:
            my_list[i] = 1

    res = sorted(list(my_list))
    print(res)


sort_words()
